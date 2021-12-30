#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'reverseArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY a as parameter.
#

# reverse, reversed 내장함수도 있음
def reverseArray(a):
    result = []
    for i in range(len(a)-1, -1, -1):
        result.append(a[i])
    return result

if __name__ == '__main__':
    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr)
    print(res)