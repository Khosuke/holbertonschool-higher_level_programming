#!/usr/bin/python3
"""
This module defines one function: pascal_triangle().
"""


def pascal_triangle(n):
    """
    This function create a Pascal Triangle.
    Args:
        n: The size of the Pascal Triangle.
    Returns:
        A list of lists to represent a Pascal Triangle.
    """
    if n <= 0:
        return []

    my_triangle = [[1]]

    for i in range(1, n):
        prev_list = my_triangle[-1]
        current_list = [1]
        for j in range(1, i):
            num1 = prev_list[j-1]
            num2 = prev_list[j]
            current_list.append(num1 + num2)
        current_list.append(1)
        my_triangle.append(current_list)
    return my_triangle
