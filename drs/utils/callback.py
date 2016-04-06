"""
Authors:    Porebski Elvis      C00170343
            Tyrakowski Bartosz  C00155128
Date:       February, 2016
"""


def console_callback(record_number, total):
    if record_number < 1000 or record_number % 1000 == 0 or record_number == total:
        print('Current Record: {}/{}'.format(record_number, total))
