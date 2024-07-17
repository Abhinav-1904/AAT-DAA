#!/bin/python3
import math
import os
import random
import re
import sys
#
# Complete the 'quickSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#
def partition(arr):
    pivot = arr[0]
    less_than_pivot = []
    greater_than_pivot = []

    for value in arr[1:]:
        if value <= pivot:
            less_than_pivot.append(value)
        else:
            greater_than_pivot.append(value)
    
    new_arr = less_than_pivot + [pivot] + greater_than_pivot
    return new_arr

if __name__ == "__main__":
    m = int(input())
    ar = list(map(int, input().strip().split()))
    result = partition(ar)
    print(' '.join(map(str, result)))
