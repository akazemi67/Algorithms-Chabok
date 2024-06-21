#!/bin/python3
# Problem's Link: https://www.hackerrank.com/challenges/ctci-merge-sort/problem

import math
import os
import random
import re
import sys


def merge(arr, aux, left, mid, right):
    # Copying Array Items
    for i in range(left, right+1):
        aux[i] = arr[i]

    i, j = left, mid + 1
    cnt = 0
    for k in range(left, right + 1):
        if i > mid:
            arr[k] = aux[j]
            j += 1
        elif j > right:
            arr[k] = aux[i]
            i += 1
        elif aux[i] <= aux[j]:
            arr[k] = aux[i]
            i += 1
        else:
            arr[k] = aux[j]
            j += 1
            cnt += (mid-i+1)
    return cnt


def merge_sort(arr, aux, left, right):
    if left >= right:
        return 0

    mid = (left + right) // 2
    a = merge_sort(arr, aux, left, mid)
    b = merge_sort(arr, aux, mid + 1, right)
    c = merge(arr, aux, left, mid, right)
    return a+b+c


def countInversions(arr):
    n = len(arr)
    aux = [0]*n
    return merge_sort(arr, aux, 0, n-1)
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = countInversions(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
