#!/bin/python3
# Problem's Link: https://www.hackerrank.com/challenges/recursive-digit-sum/problem

import math
import os
import random
import re
import sys


def recursive_supertDigit(n):
    if n%10 == n:
        return n 
    res = 0
    while n>0:
        res += (n%10)
        n = n//10
        
    return recursive_supertDigit(res)


def superDigit(n, k):
    res = 0
    for c in n:
        res += ord(c)-ord('0')
    return recursive_supertDigit(res * k)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
