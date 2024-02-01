#!/usr/bin/python3
"""
a file that validates UTF codees
"""


def validUTF8(data):
    """ a function that validates UTF code """
    def is_follow_byte(byte):
        """ a helper function that helps to iterate through inputs """
        return (byte & 0b11000000) == 0b10000000

    i = 0
    while i < len(data):
        num_bytes = 0
        mask = 0b10000000
        while (data[i] & mask):
            num_bytes += 1
            mask >>= 1

        if num_bytes == 1 or num_bytes > 4:
            return False
        for j in range(1, num_bytes):
            i += 1
            if i >= len(data) or not is_follow_byte(data[i]):
                return False
        i += 1

    return True
