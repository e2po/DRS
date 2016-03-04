"""
Authors:    Porebski Elvis      C00170343
            Tyrakowski Bartosz  C00155128
Date:       March 24th, 2016
"""

import os
from unittest import TestCase

from drs.mft.mfttable import MftTable
from drs.partition.ntfspartition import NtfsPartition


class TestMftTable(TestCase):
    partition = NtfsPartition(path=os.path.dirname(os.path.abspath(__file__)) + "/../../usb_stick.img",
                              size=4050649088,
                              label='usb stick')
    mft_table = MftTable.load_mft_table(partition)

    def test_load_mft_table(self):
        expected_mft_data_runs = [(19, 4)]

        self.assertListEqual(expected_mft_data_runs, self.mft_table.data_runs)  # MFT stored on 19 clusters (4-22)
        self.assertEqual(66, self.mft_table.record_count)  # 66 records in MFT

    def test_get_record(self):
        active_einstein_jpg_file_record = self.mft_table.get_record(65)
        deleted_turing_jpg_file_record = self.mft_table.get_record(65)

        einstein_jpg_size = 37647
        einstein_jpg_data_runs = [(10, 127848)]

        turing_jpg_size = 37647
        turing_jpg_data_runs = [(10, 127848)]

        self.assertEqual(einstein_jpg_size, active_einstein_jpg_file_record.attrs['size'])
        self.assertEqual(einstein_jpg_data_runs, active_einstein_jpg_file_record.attrs['data_runs'])

        self.assertEqual(turing_jpg_size, deleted_turing_jpg_file_record.attrs['size'])
        self.assertEqual(turing_jpg_data_runs, deleted_turing_jpg_file_record.attrs['data_runs'])

    def test_get_size(self):
        self.assertEqual(66 * 1024, self.mft_table.get_size())  # 66 records, 1024 bytes each
