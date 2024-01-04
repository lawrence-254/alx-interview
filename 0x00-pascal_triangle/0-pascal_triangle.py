#!/usr/bin/python3
"""
A code that prints pythagoras triangle/right angle triangle
"""
def pascal_triangle(n):
    '''
    Check if n is less than or equal to 0
    Return an empty list if n is not a positive integer
    '''
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1]
        if triangle:
            last_row = triangle[-1]
            row.extend([sum(pair) for pair in zip(last_row, last_row[1:])])
            row.append(1)
        triangle.append(row)

    return triangle
