#!/usr/bin/python3
"""A python script that checks for sequencial numbering of boxes"""


def canUnlockAll(boxes):
    opened = set([0])
    closed = set(boxes[0]).difference(set([0]))
    n = len(boxes)

    while len(closed) > 0:
        check = closed.pop()
        if check >= n or check < 0 or not check:
            continue
        if check not in opened:
            closed = closed.union(boxes[check])
            opened.add(check)
    return n == len(opened)
