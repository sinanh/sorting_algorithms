#!/usr/bin/python
""" Merge Sort """

def mergesort(alist):
    buffer = [None] * len(alist)
    return mergesort_helper(alist, buffer, 0, len(alist)-1 )


def mergesort_helper(alist, buffer, low, high):

    if low < high:
        middle = (low + high) // 2
        mergesort_helper(alist, buffer, low, middle)
        mergesort_helper(alist, buffer, middle+1, high)
        merge(alist, buffer, low, middle, high)
    return alist

def merge(alist, buffer, low, middle, high):
    for i in range(low, high + 1):
        buffer[i] = alist[i]

    buffer_left = low
    buffer_right = middle+1
    current = low

    while buffer_left <= middle and buffer_right <= high:
        if buffer[buffer_left] <= buffer[buffer_right]:
            alist[current] = buffer[buffer_left]
            buffer_left += 1
        else:
            alist[current] = buffer[buffer_right]
            buffer_right += 1
        current += 1

        #copy rest of the lest side of the arra to the target array

        remaining = middle - buffer_left
        for i in range(0, remaining+1):
            alist[current + i] = buffer[buffer_left+i]
