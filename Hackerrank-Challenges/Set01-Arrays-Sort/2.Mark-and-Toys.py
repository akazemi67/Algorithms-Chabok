#!/bin/python3
# Problem's Link: https://www.hackerrank.com/challenges/mark-and-toys/problem

import math
import os
import random
import re
import sys

def maximumToys(prices, k):
    sorted_prices = sorted(prices)
    res, i = 0, 0
    n = len(sorted_prices)
    while sorted_prices[i]<=k and i<n:
        k -= sorted_prices[i]
        res += 1
        i += 1
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()
