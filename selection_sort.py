#!/usr/bin/python
""" Selection Sort """


def selection_sort(alist):
    """
    sorts a given list in an ascending order.

    Parameters:
    alist: the input list that contains the numbers.
    """

    for i in range(len(alist)):
        min_idx = i

        for j in range(i+1, len(alist)):
            if alist[j] < alist[min_idx]:
                min_idx = j
        alist[i], alist[min_idx] = alist[min_idx], alist[i]
    return alist
