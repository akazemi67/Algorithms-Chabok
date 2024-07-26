#!/bin/python3
# Problem's Link: https://www.hackerrank.com/challenges/equal-stacks/problem

import math
import os
import random
import re
import sys


# Complete the 'equalStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h1
#  2. INTEGER_ARRAY h2
#  3. INTEGER_ARRAY h3
#
def calc_sums(arr):
    i = len(arr)-2
    while i>=0:
        arr[i] += arr[i+1]
        i -= 1
    
def binSearch(arr, l, r, x):
    if l>r:
        return -1
    
    m = (l+r)//2
    if arr[m]==x:
        return m
    if arr[m]>x:
        return binSearch(arr, m+1, r, x)
    return binSearch(arr, l, m-1, x)
    
    
def equalStacks(h1, h2, h3):
    calc_sums(h1)
    calc_sums(h2)
    calc_sums(h3)
    
    for i in range(len(h1)):
        s2 = binSearch(h2, 0, len(h2)-1, h1[i])
        s3 = binSearch(h3, 0, len(h3)-1, h1[i])
        if s2>=0 and s3>=0:
            return h1[i]
    return 0


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n1 = int(first_multiple_input[0])

    n2 = int(first_multiple_input[1])

    n3 = int(first_multiple_input[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()

