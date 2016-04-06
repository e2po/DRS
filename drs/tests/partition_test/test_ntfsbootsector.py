"""
Authors:    Porebski Elvis      C00170343
            Tyrakowski Bartosz  C00155128
Date:       February, 2016
"""

from unittest import TestCase
from drs.partition.ntfsbootsector import NtfsBootSector
import os


class TestNtfsBootSector(TestCase):
    CLUSTER_SIZE_IN_BYTES = 4096
    MFT_START_OFFSET_IN_BYTES = 16384
    MFT_RECORD_SIZE_IN_BYTES = 1024

    # open
    with open(os.path.dirname(os.path.abspath(__file__)) + "/../../usb_stick.img", 'rb') as f:
        data = f.read(512)

    boot_sector = NtfsBootSector.from_raw(data=data)

    def test_get_cluster_size(self):
        self.assertEqual(self.boot_sector.get_cluster_size(), self.CLUSTER_SIZE_IN_BYTES)

    def test_get_mft_start_offset(self):
        self.assertEqual(self.boot_sector.get_mft_start_bytes_offset(), self.MFT_START_OFFSET_IN_BYTES)

    def test_calculate_mft_record_size(self):
        self.assertEqual(self.boot_sector.mft_record_size, self.MFT_RECORD_SIZE_IN_BYTES)
