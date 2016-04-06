"""
Authors:    Porebski Elvis      C00170343
            Tyrakowski Bartosz  C00155128
Date:       February, 2016
"""

from drs.partition.ntfspartition import NtfsPartition


class Bitmap:
    def __init__(self, partition: NtfsPartition, bitmap_data_runs: list):
        self.partition = partition
        self.bitmap_data_runs = bitmap_data_runs

    def check_clusters_alloc(self, clusters_data_runs):
        for (length, lcn) in clusters_data_runs:
            for i in range(length):
                if self.check_cluster_alloc(lcn + i):
                    return True
        return False

    def check_cluster_alloc(self, n):
        # which bit in which byte stores alloc status for our cluster?
        byte_number = n // 8
        bit_offset = n % 8

        sector = byte_number // self.partition.boot_sector.bytes_per_sector
        byte_offset = byte_number % self.partition.boot_sector.bytes_per_sector

        # (length, lcn) = self.bitmap_data_runs[0][1]
        bitmap_offset = self.bitmap_data_runs[0][1] * self.partition.boot_sector.get_cluster_size()

        offset = sector * self.partition.boot_sector.bytes_per_sector + bitmap_offset
        data = self.partition.read_data(offset, self.partition.boot_sector.bytes_per_sector)
        return data[byte_offset] >> bit_offset & 1 == 1
