#!/usr/bin/python3
"""A python script that checks for sequencial numbering of boxes"""


def canUnlockAll(boxes):
    opened = set()
    pile_list = [0]

    while pile_list:
        current_box = pile_list.pop()
        opened.add(current_box)

        for k in boxes[current_box]:
            if k not in opened and k < len(boxes):
                pile_list.append(k)

    return len(opened) == len(boxes)
