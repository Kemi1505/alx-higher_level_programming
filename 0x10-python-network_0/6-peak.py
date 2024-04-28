#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Finds the peak in a list of just integers"""

    if not list_of_integers:
        return None

    a = 0
    b = len(list_of_integers) - 1

    while a < b:
        c = (a + b) // 2

        if list_of_integers[c] < list_of_integers[c + 1]:
            a = c + 1
        else:
            b = c

    return list_of_integers[a]
