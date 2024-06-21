#!/bin/python3
# Problem's Link: https://www.hackerrank.com/challenges/alternating-characters/problem

import math
import os
import random
import re
import sys

def alternatingCharacters(s):
    prev = ''
    res = 0
    for c in s:
        if c == prev:
            res += 1
        else:
            prev = c
    return res
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
