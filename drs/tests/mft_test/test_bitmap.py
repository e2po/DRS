"""
Authors:    Porebski Elvis      C00170343
            Tyrakowski Bartosz  C00155128
Date:       February, 2016
"""

import os
from unittest import TestCase

from drs.mft.bitmap_alloc_clusters import Bitmap
from drs.mft.mfttable import MftTable
from drs.partition.ntfspartition import NtfsPartition


class TestBitmap(TestCase):
    partition = NtfsPartition(path=os.path.dirname(os.path.abspath(__file__)) + "/../../usb_stick.img",
                              size=4050649088,
                              label='usb stick')
    mft_table = MftTable.load_mft_table(partition)
    bitmap_record = mft_table.get_record(6)

    data_runs = [(31, 123623)]
    bitmap = Bitmap(partition=partition, bitmap_data_runs=data_runs)

    def test_check_cluster_alloc(self):
        data_runs = [(31, 123623)]
        bitmap = Bitmap(partition=self.partition, bitmap_data_runs=data_runs)

        self.assertTrue(bitmap.check_cluster_alloc(4))
        self.assertFalse(bitmap.check_cluster_alloc(127848))

    def test_check_clusters_alloc(self):
        alloc_data_runs = self.mft_table.get_record(64).attrs['data_runs']
        free_data_runs = self.mft_table.get_record(65).attrs['data_runs']

        self.assertTrue(self.bitmap.check_clusters_alloc(alloc_data_runs))
        self.assertFalse(self.bitmap.check_clusters_alloc(free_data_runs))
