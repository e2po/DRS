"""
Authors:    Porebski Elvis      C00170343
            Tyrakowski Bartosz  C00155128
Date:       February, 2016
"""

import os
from unittest import TestCase

from drs.mft.record import Record
from drs.partition.ntfspartition import NtfsPartition


class TestRecord(TestCase):
    partition = NtfsPartition(path=os.path.dirname(os.path.abspath(__file__)) + "/../../usb_stick.img",
                              size=4050649088,
                              label='usb stick')

    def test_is_valid(self):
        valid_record = Record(0x454c4946,
                              record_number=0,
                              seq_no=0,
                              flags=None,
                              attrs=None)
        invalid_record = Record(0xffffffff,
                                record_number=0,
                                seq_no=0,
                                flags=None,
                                attrs=None)

        self.assertTrue(valid_record.is_valid())
        self.assertFalse(invalid_record.is_valid())

    def test_is_deleted(self):
        deleted_file_record = Record(0x454c4946,
                                     record_number=0,
                                     seq_no=0,
                                     flags=0x0000,
                                     attrs=None)
        active_file_record = Record(0x454c4946,
                                    record_number=0,
                                    seq_no=0,
                                    flags=0x0001,
                                    attrs=None)

        deleted_folder_record = Record(0x454c4946,
                                       record_number=0,
                                       seq_no=0,
                                       flags=0x0003,
                                       attrs=None)
        active_folder_record = Record(0x454c4946,
                                      record_number=0,
                                      seq_no=0,
                                      flags=0x0002,
                                      attrs=None)

        self.assertTrue(deleted_file_record.is_deleted())
        self.assertFalse(active_file_record.is_deleted())

        self.assertTrue(deleted_folder_record.is_deleted())
        self.assertFalse(active_folder_record.is_deleted())

    def test_is_file(self):
        deleted_file_record = Record(0x454c4946,
                                     record_number=0,
                                     seq_no=0,
                                     flags=0x0000,
                                     attrs=None)
        active_file_record = Record(0x454c4946,
                                    record_number=0,
                                    seq_no=0,
                                    flags=0x0001,
                                    attrs=None)

        deleted_folder_record = Record(0x454c4946,
                                       record_number=0,
                                       seq_no=0,
                                       flags=0x0003,
                                       attrs=None)
        active_folder_record = Record(0x454c4946,
                                      record_number=0,
                                      seq_no=0,
                                      flags=0x0002,
                                      attrs=None)

        self.assertTrue(deleted_file_record.is_file())
        self.assertTrue(active_file_record.is_file())

        self.assertFalse(deleted_folder_record.is_file())
        self.assertFalse(active_folder_record.is_file())

    def test_from_raw(self):
        raw_data = self.partition.read_data(self.partition.boot_sector.get_mft_start_bytes_offset(), 1024)
        record = Record.from_raw(raw_data)

        # test mft entry header
        self.assertEqual(0x454c4946, record.signature)
        self.assertTrue(record.is_valid())
        self.assertFalse(record.is_deleted())
        self.assertTrue(record.is_file())

        # test $FILE_NAME attribute
        self.assertEqual('$MFT', record.attrs['file_name'])

        # test $DATA attribute
        expected_data_runs = [(19, 4)]
        self.assertTrue('data_runs' in record.attrs)
        self.assertListEqual(expected_data_runs, record.attrs['data_runs'])
        self.assertEqual(0, record.record_number)

    def test_turing_jpg_from_raw(self):
        raw_data = self.partition.read_data(81920, 1024)
        record = Record.from_raw(raw_data)

        # test mft entry header
        self.assertEqual(0x454c4946, record.signature)
        self.assertTrue(record.is_valid())
        self.assertFalse(record.is_deleted())
        self.assertTrue(record.is_file())

        # test $FILE_NAME attribute
        self.assertEqual(1, record.seq_no)
        self.assertEqual(5, record.attrs['parent_dir_file_req_no'])
        self.assertEqual(5, record.attrs['parent_dir_seq_no'])
        self.assertEqual('Alan_Turing.jpg', record.attrs['file_name'])

        # test $DATA attribute
        expected_data_runs = [(17, 123751)]
        self.assertTrue('data_runs' in record.attrs)
        self.assertListEqual(expected_data_runs, record.attrs['data_runs'])
        self.assertEqual(64, record.record_number)
