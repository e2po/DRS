from NtfsPartition import NtfsPartition
from NtfsBootSector import NtfsBootSector

__all__ = ["partitions"]

if __name__ == "__main__":
    partition = NtfsPartition('/home/elvis/PycharmProjects/DRS/usb_stick.img',
                              4050649088,
                              'usb_stick')
    boot_sector = NtfsBootSector(partition.read_data(0, 1))
    print("bytes per sector: " + str(boot_sector.bytes_per_sector))
    print("sectors per cluster: " + str(boot_sector.sectors_per_cluster))
    print("mft start offset: " + str(boot_sector.get_mft_start_offset()))
    #print("mft entry size: " + str(boot_sector.mft_entry_size))
