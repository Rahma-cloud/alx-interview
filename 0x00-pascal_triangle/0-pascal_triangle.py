#!/usr/bin/python3
"""
12-pascal_triangle Module
"""


def pascal_triangle(n):
    """
    pascal_triangle function
    Parameters:
    n (int): The number of rows for Pascal's triangle.

    Returns:
    list of lists: A list of lists representing Pascal's triangle.
    Each inner list corresponds to a row in the triangle.
    """
    my_list = []
    if n <= 0:
        return my_list

    for i in range(n):
        row = [1]
        if len(my_list) > 0:
            prev_row = my_list[-1]
            for j in range(len(prev_row) - 1):
                row.append(prev_row[j] + prev_row[j + 1])
            row.append(1)
        my_list.append(row)
    return my_list
