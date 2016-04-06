"""
Authors:    Porebski Elvis      C00170343
            Tyrakowski Bartosz  C00155128
Date:       February, 2016
"""

from drs.partition.ntfsbootsector import NtfsBootSector


class NtfsPartition:
    """
    Class representing NTFS Partition installed on a system.
    """
    def __init__(self, path, size: int, label=""):
        self.path = path
        self.size = size
        self.label = label
        self.boot_sector = NtfsBootSector.from_raw(self.read_data(0, 512))

    def read_data(self, start_pos: int, bytes_to_read: int):
        """
        Method used to read bytes from this partition.

        :param start_pos: position of read pointer within this partition.
        :param bytes_to_read: number of bytes to read from this partition.

        :return: bytes read in string.
        """
        with open(self.path, 'rb') as partition:
            partition.seek(start_pos)
            return partition.read(bytes_to_read)

    def overwrite_data(self, start_pos: int, data: bytearray):
        """
        Method used to overwrite bytes in this partition.

        :param start_pos:   position of write pointer
        :param data:    new data to be written to this partition.
        """
        with open(self.path, 'rb+') as partition:
            partition.seek(start_pos)
            partition.write(data)

    def to_json(self):
        return {
            'path': self.path,
            'size': self.size,
            'label': self.label
        }

