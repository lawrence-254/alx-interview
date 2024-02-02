#!/usr/bin/python3
'''
a method that determines if a given data set represents
a valid UTF-8 encoding
'''


def validUTF8(data):
    '''
    Return: True if data is a valid UTF-8 encoding, else return False
    A character in UTF-8 can be 1 to 4 bytes long
    The data set can contain multiple characters
    The data will be represented by a list of integers
    Each integer represents 1 byte of data, therefore you only need
        to handle the 8 least significant bits of each integer
    '''
    def isStartByte(byte):
        '''
        checks for start
        '''
        return (byte & 0b10000000) == 0b00000000

    def isContinuationByte(byte):
        '''
        checks if byte is concurrent
        '''
        return (byte & 0b11000000) == 0b10000000
    i = 0
    while i < len(data):
        num_bytes = 1
        mask = 0b10000000
        while data[i] & mask:
            num_bytes += 1
            mask >>= 1

        if num_bytes < 1 or num_bytes > 4:
            return False

        for j in range(1, num_bytes):
            if i + j >= len(data) or not isContinuationByte(data[i + j]):
                return False

        i += num_bytes

    return True
