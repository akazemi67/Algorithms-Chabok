#!/bin/python3
# Problem's Link: https://www.hackerrank.com/challenges/angry-children/problem

import math
import os
import random
import re
import sys


def maxMin(k, arr):
    barr = sorted(arr)
    n = len(arr)

    res = barr[n-1] - barr[0]
    for i in range(k-1, n):
        res = min(res, barr[i]-barr[i-k+1])
    return res
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    k = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
