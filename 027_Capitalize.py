# The "Capitalize" task: https://www.hackerrank.com/challenges/capitalize/problem


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    full_name = s.split(' ')
    return ' '.join(i.capitalize() for i in full_name)
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
