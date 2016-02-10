class MftRecord:
    """
    This class represents a single entry in the MFT.
    """
    def __init__(self, data):
        # record for file or folder
        # 1 KB large

        # holds attributes of the file
        # contains information about the location of the data blocks of the file
        # small files are completely contained in an MFT record.

        # STANDARD INFORMATION
        # FILE OR DIRECTORY NAME
        # DATA OR INDEX
        # UNUSED SPACE

        # files up to 900B are completely stored within the MFT entry.
        
        pass
