import os
import threading

from mft.mftanalyser import MftAnalyser
from mft.mfttable import MftTable
from partition.ntfspartition import NtfsPartition
from partition.partitionmanager import PartitionManager


class Drs:
    def __init__(self, partition: NtfsPartition=None, analyser: MftAnalyser=None):
        self.partition = partition
        self.analyser = analyser
        self.data_bank = dict()

    @staticmethod
    def get_partitions():
        return PartitionManager.load_partitions()

    def analyse(self, partition: NtfsPartition):
        self.partition = partition
        mft_table = MftTable.load_mft_table(partition=partition)
        analyser = MftAnalyser(mft_table=mft_table,
                               partition=self.partition)

        analyser.deleted_records = self.data_bank

        t = threading.Thread(target=analyser.analyse())
        # t = threading.Thread(target=self.background_analyse(partition=partition))
        t.start()

    def background_analyse(self, partition: NtfsPartition):
        mft_table = MftTable.load_mft_table(partition=partition)
        analyser = MftAnalyser(mft_table=mft_table,
                               partition=partition)

        analyser.deleted_records = self.data_bank
        analyser.analyse()

    def recover_record(self, record_number: int):
        self.analyser.recover_selected(record_number=record_number)


if __name__ == '__main__':
    drs = Drs()
    partitions = drs.get_partitions()
    for p in partitions:
        print(p.to_json())

    print('Choose partition to analyse: ')

    p = NtfsPartition(path=os.path.dirname(os.path.abspath(__file__)) + "/usb_stick.img",
                      size=4050649088,
                      label='usb stick')

    drs.analyse(partition=p)
    print('\n')
    print('Found ' + str(len(drs.data_bank)) + ' deleted records!')

    for deleted_record in drs.data_bank.values():
        file_name = deleted_record['data'].attrs['file_name']
        path = deleted_record['path']
        print('path: ' + path + file_name + ' record number: ' + str(deleted_record['data'].record_number))
