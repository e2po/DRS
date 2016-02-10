import subprocess
from platform import system

from partition.NtfsPartition import NtfsPartition


class PartitionManager:
    @staticmethod
    def load_partitions():
        partitions = []
        os = system()
        if os == 'Linux':
            # run lsblk to get info about ntfs partition
            cmd = subprocess.Popen("lsblk -plnb -o name,size,fstype,label | grep ntfs",
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.STDOUT,
                                   shell=True)
            # get output from STDOUT
            output, _ = cmd.communicate()
            # decode bytes & split string on new lines, making an array
            output = output.decode(encoding='UTF-8').split('\n')
            # last element is an empty string, remove it from an array
            output.pop(-1)
            # decode bytes & parse one line at a time
            for line in output:
                # split string in half when space is found
                parsed_line = line.split()
                # create partition
                partition = NtfsPartition(
                    parsed_line[0],             # partition path
                    int(parsed_line[1]),             # partition size
                    ''.join(parsed_line[3:]))   # partition label
                # add this partition to a list
                partitions.append(partition)

        elif os == 'Windows':
            # TODO: research how to get partition in Windows
            pass
        elif os == 'Darwin':
            # TODO: research how to get partition in Mac
            pass
        return partitions
