#!/bin/python3
# Problem's Link: https://www.hackerrank.com/challenges/pairs/problem

import math
import os
import random
import re
import sys


def recursive_bin_search(arr, x, left, right):
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == x:
        return mid
    if arr[mid] < x:
        return recursive_bin_search(arr, x, mid + 1, right)
    return recursive_bin_search(arr, x, left, mid - 1)


def pairs(k, arr):
    barr = sorted(arr)
    res = 0
    n = len(barr)
    for i in range(n):
        x = barr[i] + k
        if recursive_bin_search(barr, x, i+1, n-1)>=0:
            res += 1
    return res
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
