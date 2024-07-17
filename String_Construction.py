#!/bin/python3
import math
import os
import random
import re
import sys
#
# Complete the 'stringConstruction' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def stringConstruction(s):
    unique_chars = set(s)
    return len(unique_chars)

def processTestCases(test_cases):
    results = []
    for s in test_cases:
        result = stringConstruction(s)
        results.append(result)
    return results


if __name__ == "__main__":
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])  
    test_cases = data[1:]
    
    results = processTestCases(test_cases)
    
    for res in results:
        print(res)
