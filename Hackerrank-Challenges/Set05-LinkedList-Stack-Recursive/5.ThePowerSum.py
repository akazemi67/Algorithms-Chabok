#!/bin/python3
# Problem's Link: https://www.hackerrank.com/challenges/the-power-sum/problem

import math
import os
import random
import re
import sys

#
# Complete the 'powerSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER X
#  2. INTEGER N
#
def rec(rem, num, N):
    if rem==0:
        return 1
    if rem<0:
        return 0
    
    res = 0
    for i in range(num, rem):
        temp = i**N
        if temp<=rem:
            res += rec(rem-temp, i+1, N)
    return res

def powerSum(X, N):
    return rec(X, 1, N)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    X = int(input().strip())

    N = int(input().strip())

    result = powerSum(X, N)

    fptr.write(str(result) + '\n')

    fptr.close()
