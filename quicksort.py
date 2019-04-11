#!/usr/bin/python
""" Quick Sort """
def quicksort(alist=None):
    return quicksort_helper(alist, 0, len(alist)-1)

def quicksort_helper(alist, left, right):
    #print("list: {}, left: {}, right: {}".format(alist, left, right))
    idx = partition(alist, left, right)

    if left < idx-1:
        quicksort_helper(alist, left, idx-1)
    if idx < right:
        quicksort_helper(alist, idx, right)
    return alist


def partition(alist, left, right):
    pivot = alist[(left+right)//2]

    while left <= right:
        while alist[left] < pivot:
            left += 1

        while alist[right] > pivot:
            right -= 1
        if left <= right:
            alist[left], alist[right] = alist[right], alist[left]
            left += 1
            right -= 1
    return left
