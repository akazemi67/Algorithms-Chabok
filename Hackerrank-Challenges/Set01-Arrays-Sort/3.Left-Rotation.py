#!/bin/python3
# Problem's Link: https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem

import math
import os
import random
import re
import sys

def rotLeft(a, d):
    n = len(a)
    res = [0]*n
    for i in range(n):
        j = (i-d+n)%n
        res[j] = a[i]
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
