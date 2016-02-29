# from unittest import TestCase
#
# from mft.record import MftRecord
#

# class TestMftRecord(TestCase):
#     raw_data = open('mft0.img', 'rb').read(1024)
#     mft_record = MftRecord(raw_data)
#
#     def test_should_be_valid(self):
#         self.assertTrue(self.mft_record.is_valid())
#
#     def test_should_not_be_deleted(self):
#         self.assertFalse(self.mft_record.is_deleted())
#
#     def test_should_be_file(self):
#         self.assertTrue(self.mft_record.is_file())
#
#     def test_data_runs(self):
#         # self.mft_record.get_data_runs()
#         print(self.mft_record.sss)
