"""
Authors:    Porebski Elvis      C00170343
            Tyrakowski Bartosz  C00155128
Date:       March 24th, 2016
"""

import os
from unittest import TestCase

from drs.mft.mftanalyser import MftAnalyser
from drs.mft.mfttable import MftTable
from drs.partition.ntfspartition import NtfsPartition
from drs.utils.callback import console_callback


class TestMftAnalyser(TestCase):
    partition = NtfsPartition(path=os.path.dirname(os.path.abspath(__file__)) + "/../../usb_stick.img",
                              size=4050649088,
                              label='usb stick')
    mft_table = MftTable.load_mft_table(partition)
    analyser = MftAnalyser(mft_table=mft_table, partition=partition)

    def test_analyse(self):
        self.analyser.analyse(callback=console_callback)
        self.assertEqual(1, len(self.analyser.deleted_records.keys()))

    def test_build_abs_path(self):
        record = self.mft_table.get_record(64)
        parent_seq_no = record.attrs['parent_dir_seq_no']
        parent_record_number = record.attrs['parent_dir_file_req_no']
        path = self.analyser.build_abs_path(seq_no=parent_seq_no,
                                            record_number=parent_record_number)

        self.assertFalse(path['is_orphan'])
        self.assertListEqual([5], path['rec_no'])
        self.assertListEqual(['/'], path['dir_name'])

    def test_recover_selected(self):
        deleted_record = self.mft_table.get_record(65)
        self.assertTrue(deleted_record.is_deleted())

        self.mft_table.activate_record(65)
        activated_deleted_record = self.mft_table.get_record(65)
        self.assertFalse(activated_deleted_record.is_deleted())

        flag_offset = 22
        record_offset = 65 * 1024 + self.partition.boot_sector.get_mft_start_bytes_offset()

        record = bytearray(self.partition.read_data(record_offset, 1024))
        record[flag_offset] &= 0  # change lsb to 1
        self.partition.overwrite_data(record_offset, record)

        record_deleted_again = self.mft_table.get_record(65)
        self.assertTrue(record_deleted_again.is_deleted())

