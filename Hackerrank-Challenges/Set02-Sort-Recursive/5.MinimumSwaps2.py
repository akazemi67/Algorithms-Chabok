#!/bin/python3
# Problem's Link: https://www.hackerrank.com/challenges/minimum-swaps-2/problem

import math
import os
import random
import re
import sys


def minimumSwaps(arr):
    n = len(arr)
    indices = {}
    for i in range(n):
        indices[arr[i]] = i
        
    res = 0
    for i in range(n):
        if arr[i] != i+1:
            item = arr[i]
            j = indices[i+1]
            
            arr[i], arr[j] = i+1, item
            indices[i+1] = i
            indices[item] = j
            
            res += 1
            
    return res
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
