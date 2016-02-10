import struct


class NtfsBootSector:
    """
    This class holds information about NTFS partition extracted from that partition's boot sector.
    """
    def __init__(self, data):
        self.bytes_per_sector = struct.unpack('<H', data[11:13])[0]
        self.sectors_per_cluster = struct.unpack('<B', data[13:14])[0]
        self.total_sectors = struct.unpack("<Q", data[40:48])[0]
        self.mft_start = struct.unpack("<Q", data[48:56])[0]
        self.mft_record_size = self.calculate_mft_record_size(struct.unpack("<b", data[64:65])[0])

    def get_cluster_size(self):
        """
        Calculate the size of a cluster
        :return: int representing size of cluster in bytes
        """
        return self.bytes_per_sector * self.sectors_per_cluster

    def get_mft_start_offset(self):
        """
        Calculate the location of the MFT
        :return: int representing a byte offset to the MFT
        """
        return self.get_cluster_size() * self.mft_start

    def calculate_mft_record_size(self, n):
        if n < 0:
            return 2**-n
        return self.sectors_per_cluster * n
