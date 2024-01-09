#!/usr/bin/python3
"""
You have n number of locked boxes in front of you
Each box is numbered sequentially from 0 to n - 1
and each box may contain keys to the other boxes.
"""


def canUnlockAll(boxes):
    num_boxes = len(boxes)
    visited = [False] * num_boxes
    visited[0] = True

    def dfs(box_index):
        visited[box_index] = True
        for key in boxes[box_index]:
            if not visited[key]:
                dfs(key)

    dfs(0)

    return all(visited)
