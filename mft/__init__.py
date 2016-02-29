from mft.mftanalyser import MftAnalyser
from partition.ntfspartition import NtfsPartition
from partition.ntfsbootsector import NtfsBootSector
import os

__all__ = ["partition"]

if __name__ == "__main__":
    PARTITION_PATH = (os.path.dirname(os.path.abspath(__file__)) + "/../usb_stick.img")
    PARTITION_SIZE = 4050649088
    PARTITION_LABEL = 'usb_stick'

    partition = NtfsPartition(PARTITION_PATH,    # path
                              PARTITION_SIZE,   # size in bytes
                              'usb_stick')      # label
    boot_sector = NtfsBootSector(partition.read_data(0, 1))
    print("bytes per sector: " + str(boot_sector.bytes_per_sector))
    print("sectors per cluster: " + str(boot_sector.sectors_per_cluster))
    print("mft start offset: " + str(boot_sector.get_mft_start_offset()))
    print("mft entry size: " + str(boot_sector.mft_record_size))

    mft_analyser = MftAnalyser(partition)
    mft_analyser.analyse()
