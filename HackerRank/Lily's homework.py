#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque

#
# Complete the 'lilysHomework' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def count(arr, sort):
    amap = {}
    # pos map
    for i in range(len(arr)):
        amap[arr[i]] = i
    cnt = 0
    # asc - O(N)
    for i in range(len(arr)):
        if arr[i] != sort[i]:
            # swap
            cnt += 1
            pos = amap[sort[i]]
            arr[i], arr[pos] = sort[i], arr[i]
            # pos update
            amap[arr[pos]] = pos
            amap[arr[i]] = i
    return cnt

def lilysHomework(arr):
    # Write your code here
    asc = count(arr.copy(), sorted(arr))
    desc = count(arr.copy(), sorted(arr, reverse=True))
    return min(asc, desc)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = lilysHomework(arr)

    fptr.write(str(result) + '\n')

    fptr.close()