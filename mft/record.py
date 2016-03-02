import struct

from mft.attributes import AttributeHeader, NonResidentAttribute, FileNameAttribute


class Record:
    """
    This class represents a single entry in the MFT.

    """

    def __init__(self, signature, seq_no: int, record_number: int, flags, attrs):
        self.signature = signature
        self.seq_no = seq_no
        self.record_number = record_number
        self.flags = flags
        self.attrs = attrs

    def is_valid(self):
        return self.signature == 0x454c4946

    def is_deleted(self):
        """
        Little endian   Big endian      Description
        -------------------------------------------------
        0x0000          0x0000          deleted file
        0x0300          0x0003          deleted directory

        :return: bool
        """

        return self.flags in [0x0000, 0x0003]

    def is_file(self):
        """
        Little endian   Big endian      Description
        -------------------------------------------------
        0x0000          0x0000          deleted file
        0x0001          0x0001          allocated file

        :return: bool
        """
        return self.flags in [0x0000, 0x0001]

    def is_directory(self):
        """
        Determines if this record represents a directory in a NTFS file system.
        :return: True is this record is a directory
        """
        # if it is not a file, it must be a directory
        return not self.is_file()

    @staticmethod
    def from_raw(data, record_size=1024):
        signature = struct.unpack('<I', data[:4])[0]  # first element in tuple
        seq_no = struct.unpack('<H', data[16:18])[0]
        first_attr_offset = struct.unpack('<H', data[20:22])[0]
        flags = struct.unpack('<H', data[22:24])[0]
        record_number = struct.unpack('<L', data[44:48])[0]
        attrs = dict()

        # offset to first attribute
        ptr = first_attr_offset

        while ptr < record_size:
            if data[ptr:ptr+4] == b'\xff\xff\xff\xff':
                break
            header = AttributeHeader.from_raw(data=data[ptr:])

            if header.attr_type_id == 0x80 and header.non_resident_flag == 0x01:
                data_attr = NonResidentAttribute.from_raw(data=data[ptr:ptr+header.attr_length])
                data_runs_offset = data_attr.data_runs_offset
                attrs['data_runs'] = unpack_data_runs(data[ptr+data_runs_offset:])
                attrs['size'] = data_attr.attr_content_actual_size

            if header.attr_type_id == 0x30 and header.non_resident_flag == 0x00:
                attr_data_offset = int.from_bytes(data[ptr+20:ptr+22], byteorder='little')
                file_name_attr = FileNameAttribute.from_raw(data=data[ptr+attr_data_offset:ptr+header.attr_length])
                attrs['parent_dir_file_req_no'] = file_name_attr.parent_dir_file_rec_no
                attrs['parent_dir_seq_no'] = file_name_attr.parent_dir_seq_no
                attrs['file_name'] = file_name_attr.name

            ptr += header.attr_length

        return Record(signature=signature,
                      seq_no=seq_no,
                      record_number=record_number,
                      flags=flags,
                      attrs=attrs)


def unpack_data_runs(data):
    data_runs = []
    ptr = 0
    prev = 0
    while ord(data[ptr:ptr+1]) != 0x00:
        bits = bin(ord(data[ptr:ptr+1]))[2:].rjust(8, '0')
        bytes_length = int(bits[4:], 2)

        bytes_offset = int(bits[:4], 2)

        length = int.from_bytes(data[ptr+1:ptr+1+bytes_length], byteorder='little')
        lcn = int.from_bytes(data[ptr+1+bytes_length:ptr+1+bytes_length+bytes_offset], byteorder='little', signed=True)
        data_run = (length,
                    lcn + prev)
        prev += lcn

        data_runs.append(data_run)
        ptr += 1+bytes_length+bytes_offset
    return data_runs





