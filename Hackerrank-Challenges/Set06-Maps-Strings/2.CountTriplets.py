#!/bin/python3
# Problem's Link: https://www.hackerrank.com/challenges/count-triplets-1/problem

import math
import os
import random
import re
import sys
from collections import defaultdict


# Complete the countTriplets function below.
def countTriplets(arr, r):
    rights = defaultdict(int)
    lefts = defaultdict(int)
    for x in arr:
        rights[x] += 1
    
    result = 0
    for x in arr:
        rights[x] -= 1
        if x%r == 0:
            result += lefts[x//r] * rights[x*r]
            
        lefts[x] += 1
        
    return result
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()

