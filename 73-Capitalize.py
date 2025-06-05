#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    """
    parts = s.split()
    result = ""
    for part in parts:
        result += part[0].upper() + part[1:] + " "
    """
    new_input = list(map(str,s.split()))
    result_string = s
    for i in new_input:
        result_string = result_string.replace(i,i.capitalize())
    return result_string
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
