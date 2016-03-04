"""
Authors:    Porebski Elvis      C00170343
            Tyrakowski Bartosz  C00155128
Date:       March 24th, 2016
"""

from drs.mft.record import Record
from drs.partition.ntfspartition import NtfsPartition


class MftTable:
    def __init__(self, partition: NtfsPartition, record_count: int, mft_data_runs: list):
        self.partition = partition
        self.record_count = record_count
        self.data_runs = mft_data_runs
        self.record_size = partition.boot_sector.mft_record_size
        self.cluster_size = partition.boot_sector.get_cluster_size()
        self.records_per_cluster = partition.boot_sector.get_cluster_size() / self.record_size

    def get_record(self, record_number: int):
        """
        Return nth record from MFT.

        :param record_number: nth record in MFT.
        :return: Record object representing nth record in MFT.
        """
        offset = 0
        for (length, lcn) in self.data_runs:
            max_record_no = int(length * self.records_per_cluster)
            if max_record_no <= record_number:
                record_number -= max_record_no
                # offset = lcn * self.cluster_size

            else:
                offset = int(lcn * self.cluster_size)
                break

        offset += record_number * self.record_size
        # offset += self.partition.boot_sector.get_mft_start_bytes_offset()
        # offset = record_number * self.record_size + self.partition.boot_sector.get_mft_start_bytes_offset()
        return Record.from_raw(self.partition.read_data(offset, self.record_size))

    def activate_record(self, record_number: int):
        flag_offset = 22
        record_offset = record_number * self.record_size + self.partition.boot_sector.get_mft_start_bytes_offset()

        record = bytearray(self.partition.read_data(record_offset, self.record_size))
        record[flag_offset] |= 1  # change lsb to 1
        self.partition.overwrite_data(record_offset, record)

    def get_size(self):
        """
        Calculate number of records in Master File Table.

        Total number of clusters used to store MFT is divided by number of records per cluster.

        :return: int: number of records in MFT.
        """
        return self.record_count * self.record_size

    @staticmethod
    def load_mft_table(partition: NtfsPartition):
        """
        Load MFT from partition and return MftTable object.

        :param partition: NtfsPartition object that represents partition.
        :return: MftTable object.
        """
        # location of mft
        mft_start_bytes_offset = partition.boot_sector.get_mft_start_bytes_offset()
        # size of each mft record
        record_size = partition.boot_sector.mft_record_size
        # record describing mft
        mft_record = Record.from_raw(partition.read_data(mft_start_bytes_offset,
                                                         record_size))

        record_count = int(mft_record.attrs['size'] / record_size)

        # return MFtTable object
        return MftTable(partition=partition,
                        record_count=record_count,
                        mft_data_runs=mft_record.attrs['data_runs'])        # return MFtTable object
