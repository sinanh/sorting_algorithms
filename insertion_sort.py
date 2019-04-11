#!/usr/bin/python
""" Insertion Sort """

def insertion_sort(alist):
    """
    sorts a given list in an ascending order using insertion sort algorithm.

    Parameters:
    alist: the input list that contains the numbers.
    """

    for i in range(0, len(alist)):
        j = i-1
        while alist[j+1] < alist[j] and j >= 0:
            alist[j], alist[j+1] = alist[j+1], alist[j]
            j = j - 1
    return alist
