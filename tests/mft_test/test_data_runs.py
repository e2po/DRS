from unittest import TestCase
from mft.record import unpack_data_runs


class TestDataRuns(TestCase):
    def test_simple_data_runs(self):
        expected = [(19, 4)]

        self.assertListEqual(expected, unpack_data_runs(b'\x11\x13\x04\x00'))

    def test_fragmented_data_runs(self):
        expected = [(0x38, 0x342573), (0x114, 0x363758), (0x42, 0x393802)]

        self.assertListEqual(expected,
                             unpack_data_runs(b'\x31\x38\x73\x25\x34\x32\x14\x01\xE5\x11\x02\x31\x42\xAA\x00\x03\x00'))

    def test_scrambled_data_runs(self):
        expected = [(0x30, 0x60), (0x10, 0x160), (0x20, 0x140)]

        self.assertListEqual(expected,
                             unpack_data_runs(b'\x11\x30\x60\x21\x10\x00\x01\x11\x20\xE0\x00'))
