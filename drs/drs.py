"""
Authors:    Porebski Elvis      C00170343
            Tyrakowski Bartosz  C00155128
Date:       February, 2016
"""

import os
import threading

from drs.mft.mftanalyser import MftAnalyser
from drs.mft.mfttable import MftTable
from drs.partition.ntfspartition import NtfsPartition
from drs.partition.partitionmanager import PartitionManager
from drs.utils.callback import console_callback


class Drs:
    def __init__(self, partition: NtfsPartition=None, analyser: MftAnalyser=None):
        self.partition = partition
        self.analyser = analyser
        self.data_bank = dict()

    @staticmethod
    def get_partitions():
        return PartitionManager.load_partitions()

    def analyse(self, partition: NtfsPartition, callback):
        self.partition = partition
        mft_table = MftTable.load_mft_table(partition=partition)
        self.analyser = MftAnalyser(mft_table=mft_table,
                                    partition=self.partition)

        self.analyser.deleted_records = self.data_bank

        t = threading.Thread(target=self.analyser.analyse(callback=callback))
        t.start()

    def recover_record(self, record_number: int):
        self.analyser.recover_selected(record_number=record_number)

    def recover_all(self):
        self.analyser.recover_all()


if __name__ == '__main__':
    drs = Drs()
    partitions = drs.get_partitions()
    for p in partitions:
        print(p.to_json())

    print('Choose partition to analyse: ')

    p = NtfsPartition(path=os.path.dirname(os.path.abspath(__file__)) + "/usb_stick.img",
                      size=4050649088,
                      label='usb stick')

    drs.analyse(partition=p, callback=console_callback)
    print('\n')
    print('Found ' + str(len(drs.data_bank)) + ' deleted records!')

    for deleted_record in drs.data_bank.values():
        file_name = deleted_record['data'].attrs['file_name']
        path = deleted_record['path']
        print('path: ' + path + file_name + ' record number: ' + str(deleted_record['data'].record_number))
