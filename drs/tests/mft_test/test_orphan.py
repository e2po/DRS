"""
Authors:    Porebski Elvis      C00170343
            Tyrakowski Bartosz  C00155128
Date:       February, 2016
"""

from unittest import TestCase

from drs.mft.mfttable import MftTable
from drs.mft.record import Record
from drs.partition.ntfspartition import NtfsPartition


class TestOrphan(TestCase):
    partition = NtfsPartition(path="/home/elvis/usb.img",
                              size=4050649088,
                              label='usb stick')
    mft_table = MftTable.load_mft_table(partition)

    def test_is_deleted(self):
        record = self.mft_table.get_record(222)
        print(record.seq_no)
        print(record.attrs)

    def getRecord(self, record_nb) -> Record:
        return self.mft_table.get_record(record_number=record_nb)