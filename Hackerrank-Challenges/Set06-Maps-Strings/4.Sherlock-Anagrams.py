#!/bin/python3
# Problem's Link: https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem

import math
import os
import random
import re
import sys
from collections import defaultdict

#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#
def sherlockAndAnagrams(s):
    counts = defaultdict(int)
    n = len(s)
    for i in range(n):
        for j in range(i, n):
            ss = s[i:j+1]
            sortedss = ''.join(sorted(ss))
            counts[sortedss] += 1
    
    result = 0
    for ss in counts:
        result += counts[ss] * (counts[ss]-1) // 2
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()

