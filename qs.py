#!/usr/bin/python

A = [5, 2, 90, 10, 35, -2, 15, 30, 7, 1, 29, 22, 20]

def partition(A, l, h):
    i = q = l
    while i < h:
        if A[i] <= A[h]:
            A[i], A[q] = A[q], A[i]
            q += 1
        i += 1

    A[h], A[q] = A[q], A[h]
    return q

def quicksort(A, l, h):
    if l >= h:
        return

    q = partition(A, l, h)
    quicksort(A, l, q - 1)
    quicksort(A, q + 1, h)

quicksort(A, 0, len(A) - 1)
print(A)
