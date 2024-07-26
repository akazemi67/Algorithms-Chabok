#!/bin/python3
# Problem's Link: https://www.hackerrank.com/challenges/ctci-bubble-sort/problem

import math
import os
import random
import re
import sys

def countSwaps(a):
    n = len(a)
    res = 0
    for i in range(n):
        for j in range(0, n-1):
            if(a[j] > a[j+1]):
                a[j], a[j+1] = a[j+1], a[j]
                res += 1
    print(f"Array is sorted in {res} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")
            

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
