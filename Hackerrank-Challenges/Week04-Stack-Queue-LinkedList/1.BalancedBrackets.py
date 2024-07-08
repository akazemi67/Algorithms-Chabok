#!/bin/python3
# Problem's Link: https://www.hackerrank.com/challenges/balanced-brackets/problem

import math
import os
import random
import re
import sys


def isBalanced(s):
    openning = "([{"
    closing = {')': '(', ']': '[', '}': '{' }
    stack = []
    for c in s:
        if c in openning:
            stack.append(c)
        elif (c in closing) and len(stack)>0 and closing[c]==stack[-1]:
            stack.pop()
        else:
            return "NO"
    return "NO" if stack else "YES"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()

