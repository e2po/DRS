"""
Authors:    Porebski Elvis      C00170343
            Tyrakowski Bartosz  C00155128
Date:       February, 2016
"""

import struct


class NtfsBootSector:
    """
    This class holds information about NTFS partition extracted from that partition's boot sector.
    """
    def __init__(self, bytes_per_sector, sectors_per_cluster, total_sectors, mft_start_lcn_offset, mft_record_size=1024):
        self.bytes_per_sector = bytes_per_sector
        self.sectors_per_cluster = sectors_per_cluster
        self.total_sectors = total_sectors
        self.mft_start_lcn_offset = mft_start_lcn_offset
        self.mft_record_size = mft_record_size

    def get_cluster_size(self):
        """
        Calculate the size of a cluster
        :return: int representing size of cluster in bytes
        """
        return self.bytes_per_sector * self.sectors_per_cluster

    def get_mft_start_bytes_offset(self):
        """
        Calculate the location of the MFT
        :return: int representing a byte offset to the MFT
        """
        return self.get_cluster_size() * self.mft_start_lcn_offset

    @staticmethod
    def calculate_mft_record_size(sectors_per_cluster, n):
        if n < 0:
            return 2**-n
        return sectors_per_cluster * n

    @staticmethod
    def from_raw(data):
        bytes_per_sector = struct.unpack('<H', data[11:13])[0]
        sectors_per_cluster = struct.unpack('<B', data[13:14])[0]
        total_sectors = struct.unpack("<Q", data[40:48])[0]
        mft_start_lcn_offset = struct.unpack("<Q", data[48:56])[0]
        mft_record_size = NtfsBootSector.calculate_mft_record_size(sectors_per_cluster=sectors_per_cluster,
                                                                   n=struct.unpack("<b", data[64:65])[0])

        return NtfsBootSector(bytes_per_sector=bytes_per_sector,
                              sectors_per_cluster=sectors_per_cluster,
                              total_sectors=total_sectors,
                              mft_start_lcn_offset=mft_start_lcn_offset,
                              mft_record_size=mft_record_size)
