#!/bin/python3
# Problem's Link: https://www.hackerrank.com/challenges/ctci-ransom-note/problem

import math
import os
import random
import re
import sys

#
# Complete the 'checkMagazine' function below.
#
# The function accepts following parameters:
#  1. STRING_ARRAY magazine
#  2. STRING_ARRAY note
#
def count_words(words, words_map):
    for w in words:
        if w in words_map:
            words_map[w] += 1
        else:
            words_map[w] = 1

def checkMagazine(magazine, note):
    mag_words = {}
    note_words = {}
    
    count_words(magazine, mag_words)
    count_words(note, note_words)
    
    for w in note_words:
        if (w not in mag_words) or (mag_words[w] < note_words[w]):
            print("No")
            return
    print("Yes")


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)

