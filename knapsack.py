#!/bin/python3
import math
import os
import random
import re
import sys
#
# Complete the 'unboundedKnapsack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#
def unboundedKnapsack(k, arr):
    arr.sort()
    dp = [0] * (k + 1)
    
    for item in arr:
        for j in range(item, k + 1):
            dp[j] = max(dp[j], item + dp[j - item])
    
    return dp[k]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for _ in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        arr = list(map(int, input().rstrip().split()))

        result = unboundedKnapsack(k, arr)

        fptr.write(str(result) + '\n')

    fptr.close()
