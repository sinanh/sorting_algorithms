#!/usr/bin/python
""" Bubble Sort """

def bubble_sort(A):
    swap = True

    while swap:
        swap = False
        for i in range(len(A)-1):

            if A[i+1] < A[i]:
                A[i], A[i+1] = A[i+1], A[i]
                swap = True
    return A
