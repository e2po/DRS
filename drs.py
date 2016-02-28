from partition.PartitionManager import PartitionManager


class Drs:
    @staticmethod
    def get_partitions():
        return PartitionManager.load_partitions()

    @staticmethod
    def analyze_mft():
        return 'ok'