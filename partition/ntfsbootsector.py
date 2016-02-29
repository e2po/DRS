import struct


class NtfsBootSector:
    """
    This class holds information about NTFS partition extracted from that partition's boot sector.
    """
    def __init__(self, bytes_per_sector, sectors_per_cluster, total_sectors, mft_start_lcn_offset, mft_record_size=1024):
        self.bytes_per_sector = bytes_per_sector
        self.sectors_per_cluster = sectors_per_cluster
        self.total_sectors = total_sectors
        self.mft_start_lcn_offset = mft_start_lcn_offset
        self.mft_record_size = mft_record_size

    def get_cluster_size(self):
        """
        Calculate the size of a cluster
        :return: int representing size of cluster in bytes
        """
        return self.bytes_per_sector * self.sectors_per_cluster

    def get_mft_start_bytes_offset(self):
        """
        Calculate the location of the MFT
        :return: int representing a byte offset to the MFT
        """
        return self.get_cluster_size() * self.mft_start_lcn_offset

    @staticmethod
    def calculate_mft_record_size(sectors_per_cluster, n):
        if n < 0:
            return 2**-n
        return sectors_per_cluster * n

    @staticmethod
    def from_raw(data):
        """
        Table 13.18. Data structure for the boot sector.
        ---------------------------------------------------------------------
        Byte Range      Description                                 Essential
        0–2             Assembly instruction to jump to boot code   No
        3–10            OEM Name                                    No
        11–12           Bytes per sector                            Yes
        13–13           Sectors per cluster                         Yes
        14–15           Reserved sectors                            No
        16–20           Unused                                      No
        21–21           Media descriptor                            No
        22–23           Unused                                      No
        24–31           Unused (Microsoft says it is not checked)   No
        32–35           Unused (Microsoft says it must be 0)        No
        36–39           Unused (Microsoft says it is not checked)   No
        40–47           Total sectors in file system                Yes
        48–55           Starting cluster address of MFT             Yes
        56–63           Starting cluster address of MFT Mirror      No
        64–64           Size of file record (MFT entry)             Yes
        65–67           Unused                                      No
        68–68           Size of index record                        Yes
        69–71           Unused                                      No
        72–79           Serial number                               No
        80–83           Unused                                      No
        84–509          Boot code                                   No
        510–511         Signature (0xaa55)                          No

        Source: [Carter 2004] File System Forensic Analysis.

        :param data: first sector of NtfsPartition
        :return: NtfsBootSector object.
        """
        bytes_per_sector = struct.unpack('<H', data[11:13])[0]
        sectors_per_cluster = struct.unpack('<B', data[13:14])[0]
        total_sectors = struct.unpack("<Q", data[40:48])[0]
        mft_start_lcn_offset = struct.unpack("<Q", data[48:56])[0]
        mft_record_size = NtfsBootSector.calculate_mft_record_size(sectors_per_cluster=sectors_per_cluster,
                                                                   n=struct.unpack("<b", data[64:65])[0])

        return NtfsBootSector(bytes_per_sector=bytes_per_sector,
                              sectors_per_cluster=sectors_per_cluster,
                              total_sectors=total_sectors,
                              mft_start_lcn_offset=mft_start_lcn_offset,
                              mft_record_size=mft_record_size)
