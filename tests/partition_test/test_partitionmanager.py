from unittest import TestCase
from partition.partitionmanager import PartitionManager
from partition.ntfspartition import NtfsPartition


class TestPartitionManager(TestCase):
    def test_load_partitions(self):
        partitions = []
        p1 = NtfsPartition("/dev/sdb1", 524288000, "SystemReserved")
        p2 = NtfsPartition("/dev/sdb2", 109832044544, "")
        p3 = NtfsPartition("/dev/sdb3", 100000000000, "MyFiles")
        partitions.append(p1)
        partitions.append(p2)
        partitions.append(p3)

        for i in range(len(partitions)):
            self.assertDictEqual(partitions[i].to_json(), PartitionManager.load_partitions()[i].to_json())
