#!/usr/bin/python3
"""
function that returns a list of lists of integer
srepresenting the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """
    receives an int
    returns a list of lists of ints
    """
    if n <= 0:
        return []
    if n == 1:
        return [[1]]
    triangle = [[1]]
    for i in range(1, n):
        line = [1]
        for j in range(1, i):
            line.append(triangle[i-1][j-1] + triangle[i-1][j])
        line.append(1)
        triangle.append(line)
    return triangle
