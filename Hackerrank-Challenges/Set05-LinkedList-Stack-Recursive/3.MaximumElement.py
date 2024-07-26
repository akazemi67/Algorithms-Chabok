#!/bin/python3
# Problem's Link: https://www.hackerrank.com/challenges/maximum-element/problem

import math
import os
import random
import re
import sys


# Complete the 'getMax' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY operations as parameter.
#
def getMax(operations):
    values = []
    maxes = []
    results = []
    
    idx = 0
    for op in operations:
        idx += 1
        if op[0]=='1':
            item = int(op.split(' ')[1])
            values.append( (idx, item) )
            if len(maxes) == 0:
                maxes.append( (idx, item) )
                continue
                
            curr_max = maxes[-1][1]
            if curr_max < item:
                maxes.append( (idx, item) )
                
        elif op[0]=='2':
            top = values[-1]
            values.pop()
            if top[0]==maxes[-1][0] and top[1]==maxes[-1][1]:
                maxes.pop()
        
        else:
            results.append(maxes[-1][1])
    
    return results
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ops = []

    for _ in range(n):
        ops_item = input()
        ops.append(ops_item)

    res = getMax(ops)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
