#!/usr/bin/python3
"""
12-pascal_triangle Module
"""


def canUnlockAll(boxes):
    """
    pascal_triangle function
    Parameters:
    n (int): The number of rows for Pascal's triangle.

    Returns:
    list of lists: A list of lists representing Pascal's triangle.
    Each inner list corresponds to a row in the triangle.
    """
    unlockedBoxes = {0}
    keysToCheck = [0]

    while keysToCheck:
        currentBox = keysToCheck.pop()
        for key in boxes[currentBox]:
            if key not in unlockedBoxes:
                unlockedBoxes.add(key)
                keysToCheck.append(key)
    return len(unlockedBoxes) == len(boxes)
