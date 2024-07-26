#!/bin/python3
# Problem's Link: https://www.hackerrank.com/challenges/frequency-queries/problem

import math
import os
import random
import re
import sys
from collections import defaultdict


def freqQuery(queries):
    data = defaultdict(int)
    rev_data = defaultdict(int)
    result = []
    
    for q in queries:
        num = q[1]
        if q[0] == 1:
            if num in data:
                rev_data[data[num]] -= 1
            data[num] += 1
            rev_data[data[num]] += 1
        elif q[0] == 2:
            if num not in data:
                continue
            rev_data[data[num]] -= 1
            data[num] -= 1
            if data[num] == 0:
                del data[num]
            else:
                rev_data[data[num]] += 1
        else:
            if (num in rev_data) and (rev_data[num]>0):
                result.append(1)
            else:
                result.append(0)
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
