#!/usr/bin/python3
'''
Minimum Operations
'''


def minOperations(n):
    '''
    returns the fewest number of operations needed to result
    in exactly n H characters.
    '''
    if not isinstance(n, int) or n <= 1:
        return 0

    ops_count = 0
    clipboard = 1

    while clipboard < n:
        if n % clipboard == 0:
            clipboard = n
        else:
            clipboard += clipboard

        ops_count += 1

    return ops_count
