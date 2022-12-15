#!/usr/bin/python3
"""0. Minimum Operations"""


def minOperations(n):
    """min operations func """
    minop = 0
    div = 2
    while isinstance(n, int) and n > 1:
        while n % div:
            div += 1
        minop += div
        n = int(n / div)
    return minop
