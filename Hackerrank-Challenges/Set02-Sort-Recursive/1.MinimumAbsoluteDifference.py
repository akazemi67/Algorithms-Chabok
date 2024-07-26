#!/bin/python3
# Problem's Link: https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem

import math
import os
import random
import re
import sys

def minimumAbsoluteDifference(arr):
    barr = sorted(arr)
    res = barr[1]-barr[0]
    for i in range(2,n):
        res = min(res, barr[i]-barr[i-1])
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
