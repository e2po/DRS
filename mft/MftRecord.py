import struct


class MftRecord:
    """
    This class represents a single entry in the MFT.
    """

    def __init__(self, raw_data):
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
        self.signature = struct.unpack('<I', raw_data[:4])[0]  # first element in tuple
        self.flags = struct.unpack('<H', raw_data[22:24])[0]
        self.first_attr_offset = struct.unpack('<H', raw_data[20:22])[0]

        if True:
            self.sss = True

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


