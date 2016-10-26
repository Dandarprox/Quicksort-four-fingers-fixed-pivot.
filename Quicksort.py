import itertools
from sys import *
setrecursionlimit(1000000)

comparaciones = 0

def QuicksortStart(A):
    Quicksort(A, 0, len(A) - 1)


def Quicksort(A, p, r):
    if p < r:
        q = Partition(A, p, r)
        Quicksort(A, p, q - 1)
        Quicksort(A, q + 1, r)

def Partition(A, p, r):
    x = A[r]
    i = p
    j = p
    while j < r:
        global comparaciones
        comparaciones += 1
        if A[j] <= x:
            exchange(i, j)
            i += 1
        j += 1
    exchange(i, r)
    return i

def exchange(i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

A = [1, 2, 3, 4]
elem = list(itertools.permutations(A))
count = 1
for x in elem:
    QuicksortStart(x)
    count += 1
    print list(x), "\t", comparaciones
    comparaciones = 0
