"""
Authors:    Porebski Elvis      C00170343
            Tyrakowski Bartosz  C00155128
Date:       February, 2016
"""

from distutils.core import setup

setup(
    name='DRS',
    version='1.0',
    packages=['drs.mft', 'drs.file', 'drs.tests', 'drs.partition'],
    url='http://eepdev.me',
    license='MIT',
    author='Elvis Porebski',
    author_email='elvisporebski@gmail.com',
    description='Data Recovery from NTFS using MFT'
)
