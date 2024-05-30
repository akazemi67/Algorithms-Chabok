#!/bin/python3
# Problem's Link: https://www.hackerrank.com/challenges/new-year-chaos/problem

import math
import os
import random
import re
import sys


def minimumBribes(q):
    n = len(q)
    i = n-1
    result = 0
    
    while i>0:
        want = i+1
        if q[i-1]==want:
            q[i-1] = q[i]
            q[i] = want
            result += 1
        elif i>1 and q[i-2]==want:
            q[i-2] = q[i-1]
            q[i-1] = q[i]
            q[i] = want
            result += 2   
        elif q[i]!=want:
            print("Too chaotic")
            return
        i -= 1

    print(result)


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)

