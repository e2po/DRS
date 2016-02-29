import struct

from mft.attributes import AttributeHeader, NonResidentAttribute, FileNameAttribute


class Record:
    """
    This class represents a single entry in the MFT.

    Table 13.1. Data structure for a basic MFT entry.
    -------------------------------------------------
    Byte Range Description Essential
    0–3     Signature ("FILE")                  No
    4–5     Offset to fixup array               Yes
    6–7     Number of entries in fixup array    Yes
    8–15    $LogFile Sequence Number (LSN)      No
    16–17   Sequence value                      No
    18–19   Link count                          No
    20–21   Offset to first attribute           Yes
    22–23   Flags (in-use and directory)        Yes
    24–27   Used size of MFT entry              Yes
    28–31   Allocated size of MFT entry         Yes
    32–39   File reference to base record       No
    40–41   Next attribute id                   No
    42–1023 Attributes and fixup values         Yes

    Source: [Carter 2004] File System Forensic Analysis.

    :param data:
    :return:

    """

    def __init__(self, signature, flags, attrs):
        self.signature = signature
        self.flags = flags
        self.attrs = attrs


        # record for file or folder
        # 1 KB large

        # holds attributes of the file
        # contains information about the location of the data blocks of the file
        # small files are completely contained in an MFT record.

        # STANDARD INFORMATION
        # FILE OR DIRECTORY NAME
        # DATA OR INDEX
        # UNUSED SPACE

        # files up to 900B are completely stored within the MFT entry.
        # self.signature = struct.unpack('<I', raw_data[:4])[0]  # first element in tuple
        # self.flags = struct.unpack('<H', raw_data[22:24])[0]
        # self.first_attr_offset = struct.unpack('<H', raw_data[20:22])[0]
        #
        # if True:
        #     self.sss = True

        # flags
        # self.in_use = struct.unpack('B', raw_record[22:23])[0]
        # self.directory = struct.unpack('B', raw_record[23:24])[0]

        # self.signature = raw_record[0:4]  # .decode('UTF-8')
        # self.fixup_array_offset = data[4:6]
        # self.fixup_array_entries = data[6:8]
        # self.lsn = data[8:16]
        # self.sequence = data[16:18]
        # self.link_count = data[18:20]

        # self.flags = data[22:24]

    def is_valid(self):
        return self.signature == 0x454c4946

    def is_deleted(self):
        """
        Little endian   Big endian      Description
        -------------------------------------------------
        0x0000          0x0000          deleted file
        0x0400          0x0004          deleted directory

        :return: bool
        """
        return self.flags == (0x0000 or 0x0004)

    def is_file(self):
        """
        Little endian   Big endian      Description
        -------------------------------------------------
        0x0000          0x0000          deleted file
        0x0001          0x0001          allocated file

        :return: bool
        """
        return self.flags == (0x0000 or 0x0001)

    # def get_data_runs(self):
    #     ptr = self.first_attr_offset
    #     while ptr < 1024:
    #
    #
    #     print(ptr)
    #     # find data runs
    #     # decode them
    #     # return list of tuples, first elem in tuple is LCN, second is number of clusters
    #     pass
    @staticmethod
    def from_raw(data, record_size=1024):
        signature = struct.unpack('<I', data[:4])[0]  # first element in tuple
        flags = struct.unpack('<H', data[22:24])[0]
        attrs = dict()

        # offset to first attribute
        ptr = struct.unpack('<H', data[20:22])[0]

        while ptr < record_size:
            if data[ptr:ptr+4] == 0xffffffff:
                break
            header = AttributeHeader.from_raw(data=data[ptr:])
            if header.attr_type_id == 0x30:
                attrs['file_name'] = FileNameAttribute.from_raw(data=data[ptr:ptr+header.attr_length])
            elif header.attr_type_id == 0x80 and header.non_resident_flag == 0x01:
                data_runs_offset = NonResidentAttribute.from_raw(data=data[ptr:ptr+header.attr_length]).data_runs_offset
                attrs['data_runs'] = data[ptr+data_runs_offset:]

            ptr += header.attr_length

        return Record(signature=signature,
                      flags=flags,
                      attrs=attrs)



def unpack_data_runs(data):
    data_runs = []
    ptr = 0
    while data[ptr:ptr] != 0x00:
        header = struct.unpack('<B', data[ptr:ptr])
        bits = bin(header)[2:].rjust(8, '0')
        bytes_length = int(bits[:4])
        bytes_offset = int(bits[4:])

        data_run = (struct.unpack())





