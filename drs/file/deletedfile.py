"""
Authors:    Porebski Elvis      C00170343
            Tyrakowski Bartosz  C00155128
Date:       February, 2016
"""


class DeletedFile:
    """
    This class represents a deleted file that can be recovered.
    """
    def __init__(self, file_name, file_type, start_offset, file_size):
        self.file_name = file_name
        self.file_type = file_type
        self.start_offset = start_offset
        self.file_size = file_size

    def to_json(self):
        """
        Convert object to json for transportation to web ui via a web socket connection.

        :return:
        """
        # todo
        print(self)
        pass

    def recover(self, partition, destination_path, new_file_name=None):
        """
        Read raw data from a partition and save it to a new file.

        :param partition: (NtfsPartition) source containing deleted file.
        :param destination_path: (string) location of recovered file.
        :param new_file_name: (string)optional parameter, specifies a new name for recovered file.
        :return: (bool) True if file recovery was successful.
        """
        if new_file_name:
            self.file_name = new_file_name
        # read raw data from partition and save it to a new file
        with open(destination_path + "/" + self.file_name, 'w+') as new_file:
            new_file.write(partition.read_data(self.start_offset, self.file_size))
            return True
