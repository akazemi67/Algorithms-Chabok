#!/bin/python3
# Problem's Link: https://www.hackerrank.com/challenges/ctci-recursive-staircase/problem

import math
import os
import random
import re
import sys


dp = {}
def stepPerms(n):
    if n<=1:
        return n
    if n==2:
        return 2
    if n==3:
        return 4
    if n in dp:
        return dp[n]
        
    dp[n] = stepPerms(n-1) + stepPerms(n-2) + stepPerms(n-3)
    return dp[n]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = int(input().strip())

    for s_itr in range(s):
        n = int(input().strip())

        res = stepPerms(n)

        fptr.write(str(res) + '\n')

    fptr.close()
