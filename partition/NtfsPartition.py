class NtfsPartition:
    def __init__(self, path, size: int, label="", sector_size=512):
        self.path = path
        self.size = size
        self.label = label
        self.sector_size = sector_size

    def read_data(self, start_pos: int, sectors_to_read: int):
        with open(self.path, 'rb') as partition:
            partition.seek(start_pos)
            return partition.read(sectors_to_read * self.sector_size)
