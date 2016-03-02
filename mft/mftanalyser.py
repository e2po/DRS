from mft.bitmap_alloc_clusters import Bitmap
from mft.mfttable import MftTable
from partition.ntfspartition import NtfsPartition


class MftAnalyser:
    def __init__(self, mft_table: MftTable, partition: NtfsPartition):
        self.mft_table = mft_table
        self.partition = partition
        self.bitmap = Bitmap(partition=partition,
                             bitmap_data_runs=self.mft_table.get_record(6).attrs['data_runs'])
        self.deleted_records = dict()

    def analyse(self):
        no_of_records = self.mft_table.record_count
        for i in range(24, no_of_records):
            record = self.mft_table.get_record(i)

            if record.is_valid() and record.is_file() and record.is_deleted():
                if 'data_runs' in record.attrs:
                    if not self.bitmap.check_clusters_alloc(record.attrs['data_runs']):

                        path = self.build_abs_path(seq_no=record.attrs['parent_dir_seq_no'],
                                                   record_number=record.attrs['parent_dir_file_req_no'])

                        result = {'data': record, 'is_orphan': path['is_orphan'], 'path': '/'.join(path['dir_name'])}

                        self.deleted_records[record.record_number] = result

    def recover_selected(self, record_number):
        if record_number in self.deleted_records.keys():
            self.mft_table.activate_record(record_number=record_number)

    def recover_all(self):
        for record_number in self.deleted_records.keys():
            self.mft_table.activate_record(record_number=record_number)

    def build_abs_path(self, seq_no: int, record_number: int, path=None):
        if path is None:
            path = {'rec_no': [], 'dir_name': [], 'is_orphan': False}
        if record_number == 5:
            # base case, tree root reached
            path['rec_no'].append(5)
            path['dir_name'].append('/')
            # path.append((5, '/', True))

            return path

        record = self.mft_table.get_record(record_number=record_number)

        if record.is_valid() and record.is_directory():
            if record.seq_no == seq_no:
                # append tuple to list
                path['rec_no'].append(record_number)
                path['dir_name'].append(record.attrs['file_name'])
                # path.append((record_number, record.attrs['file_name'], not record.is_deleted()))

                parent_record_number = record.attrs['parent_dir_file_req_no']
                parent_seq_no = record.attrs['parent_dir_seq_no']

                # tail recursive function call
                self.build_abs_path(seq_no=parent_record_number,
                                    record_number=parent_seq_no,
                                    path=path)
        path['is_orphan'] = True
        return path

