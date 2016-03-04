"""
Authors:    Porebski Elvis      C00170343
            Tyrakowski Bartosz  C00155128
Date:       March 24th, 2016
"""

import struct


class AttributeHeader:
    """
    MFT Attribute Header.

    Header is generic and standard to all attributes.
    Header identifies type of attribute, its size and name
    type of attribute
    size
    name
    flags: compressed/encrypted

    """
    def __init__(self, attr_type_id, attr_length, non_resident_flag, name_length, name_offset, flags, attr_id):
        # GENERAL HEADER: first 16 bytes of an attribute
        self.attr_type_id = attr_type_id
        self.attr_length = attr_length
        self.non_resident_flag = non_resident_flag
        self.name_length = name_length
        self.name_offset = name_offset
        self.flags = flags
        self.attr_id = attr_id

    @staticmethod
    def from_raw(data):
        attr_type_id = struct.unpack('<L', data[0:4])[0]
        attr_length = struct.unpack('<L', data[4:8])[0]
        non_residential_flag = struct.unpack('<B', data[8:9])[0]
        name_length = struct.unpack('<B', data[9:10])[0]
        name_offset = struct.unpack('<H', data[10:12])[0]
        flags = struct.unpack('<H', data[12:14])[0]
        attr_id = struct.unpack('<H', data[14:16])[0]

        return AttributeHeader(attr_type_id=attr_type_id,
                               attr_length=attr_length,
                               non_resident_flag=non_residential_flag,
                               name_length=name_length,
                               name_offset=name_offset,
                               flags=flags,
                               attr_id=attr_id)


class NonResidentAttribute:
    def __init__(self,
                 vcn_start,
                 vcn_end,
                 data_runs_offset,
                 compression_unit_size,
                 attr_content_alloc_size,
                 attr_content_actual_size,
                 attr_content_init_size):
        self.vcn_start = vcn_start
        self.vcn_end = vcn_end
        self.data_runs_offset = data_runs_offset
        self.compression_unit_size = compression_unit_size
        self.attr_content_alloc_size = attr_content_alloc_size
        self.attr_content_actual_size = attr_content_actual_size
        self.attr_content_init_size = attr_content_init_size

    @staticmethod
    def from_raw(data):
        vcn_start = struct.unpack('<Q', data[16:24])[0]
        vcn_end = struct.unpack('<Q', data[24:32])[0]
        data_runs_offset = struct.unpack('<H', data[32:34])[0]
        compression_unit_size = struct.unpack('<H', data[34:36])[0]
        attr_content_alloc_size = struct.unpack('<Q', data[40:48])[0]
        attr_content_actual_size = struct.unpack('<Q', data[48:56])[0]
        attr_content_init_size = struct.unpack('<Q', data[56:64])[0]

        return NonResidentAttribute(vcn_start=vcn_start,
                                    vcn_end=vcn_end,
                                    data_runs_offset=data_runs_offset,
                                    compression_unit_size=compression_unit_size,
                                    attr_content_alloc_size=attr_content_alloc_size,
                                    attr_content_actual_size=attr_content_actual_size,
                                    attr_content_init_size=attr_content_init_size)


class StandardInformationAttribute:
    def __init__(self,
                 creation_time=None,
                 file_altered_time=None,
                 mft_altered_time=None,
                 file_accessed_time=None,
                 flags=None,
                 max_ver_no=None,
                 ver_no=None,
                 class_id=None,
                 owner_id=None,
                 security_id=None,
                 quota_charged=None,
                 update_seq_no=None):

        self.creation_time = creation_time
        self.file_altered_time = file_altered_time
        self.mft_altered_time = mft_altered_time
        self.file_accessed_time = file_accessed_time
        self.flags = flags
        self.max_ver_no = max_ver_no
        self.ver_no = ver_no
        self.class_id = class_id
        self.owner_id = owner_id
        self.security_id = security_id
        self.quota_charged = quota_charged
        self.update_seq_no = update_seq_no

    @staticmethod
    def from_raw(data):
        creation_time = struct.unpack('<Q', data[:7])[0]
        file_altered_time = struct.unpack('<Q', data[8:15])[0]
        mft_altered_time = struct.unpack('<Q', data[16:23])[0]
        file_accessed_time = struct.unpack('<Q', data[24:31])[0]
        flags = struct.unpack('<H', data[32:35])[0]
        max_ver_no = struct.unpack('<H', data[36:39])[0]
        ver_no = struct.unpack('<H', data[40:43])[0]
        class_id = struct.unpack('<H', data[44:47])[0]
        owner_id = struct.unpack('<H', data[48:51])[0]
        security_id = struct.unpack('<H', data[52:55])[0]
        quota_charged = struct.unpack('<Q', data[56:63])[0]
        update_seq_no = struct.unpack('<Q', data[64:71])[0]

        return StandardInformationAttribute(creation_time=creation_time,
                                            file_altered_time=file_altered_time,
                                            mft_altered_time=mft_altered_time,
                                            file_accessed_time=file_accessed_time,
                                            flags=flags,
                                            max_ver_no=max_ver_no,
                                            ver_no=ver_no,
                                            class_id=class_id,
                                            owner_id=owner_id,
                                            security_id=security_id,
                                            quota_charged=quota_charged,
                                            update_seq_no=update_seq_no)


class FileNameAttribute:
    def __init__(self,
                 parent_dir_file_rec_no,
                 parent_dir_seq_no,
                 file_creation_time,
                 file_modification_time,
                 mft_modification_time,
                 file_access_time,
                 file_alloc_size,
                 file_real_size,
                 flags,
                 reparse_val,
                 name_length,
                 namespace,
                 name):

        self.parent_dir_file_rec_no = parent_dir_file_rec_no
        self.parent_dir_seq_no = parent_dir_seq_no
        self.file_creation_time = file_creation_time
        self.file_modification_time = file_modification_time
        self.mft_modification_time = mft_modification_time
        self.file_access_time = file_access_time
        self.file_alloc_size = file_alloc_size
        self.file_real_size = file_real_size
        self.flags = flags
        self.reparse_val = reparse_val
        self.name_length = name_length
        self.namespace = namespace
        self.name = name

    @staticmethod
    def from_raw(data):
        parent_dir_file_rec_no = int.from_bytes(data[:6], byteorder='little')  # struct.unpack('<Q', data[:7])[0]
        parent_dir_seq_no = int.from_bytes(data[6:8], byteorder='little')
        file_creation_time = struct.unpack('<Q', data[8:16])[0]
        file_modification_time = struct.unpack('<Q', data[16:24])[0]
        mft_modification_time = struct.unpack('<Q', data[24:32])[0]
        file_access_time = struct.unpack('<Q', data[32:40])[0]
        file_alloc_size = struct.unpack('<Q', data[40:48])[0]
        file_real_size = struct.unpack('<Q', data[48:56])[0]
        flags = struct.unpack('<L', data[56:60])[0]
        reparse_val = struct.unpack('<L', data[60:64])[0]
        name_length = struct.unpack('<B', data[64:65])[0]
        namespace = struct.unpack('<B', data[65:66])[0]
        name = data[66:66+name_length * 2].decode('utf-16')

        return FileNameAttribute(parent_dir_file_rec_no=parent_dir_file_rec_no,
                                 parent_dir_seq_no=parent_dir_seq_no,
                                 file_creation_time=file_creation_time,
                                 file_modification_time=file_modification_time,
                                 mft_modification_time=mft_modification_time,
                                 file_access_time=file_access_time,
                                 file_alloc_size=file_alloc_size,
                                 file_real_size=file_real_size,
                                 flags=flags,
                                 reparse_val=reparse_val,
                                 name_length=name_length,
                                 namespace=namespace,
                                 name=name)
