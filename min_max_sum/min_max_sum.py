"""
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

Function Description
Complete the min_max_sum function in the editor below.

Print
Print two space-separated integers on one line: the minimum sum and the maximum sum of 4 of 5 elements.

Constraints
1<=arr[i]<=10^9

Output Format

Print two space-separated long integers denoting the respective minimum and maximum values that can be calculated by summing exactly four of the five integers. (The output can be greater than a 32 bit integer.)
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'min_max_sum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def min_max_sum(arr):
    if min(arr) < 1 or max(arr) > 10 ** 9:
        return None
    arr.sort()
    print("{} {}".format(sum(arr[:4]), sum(arr[1:])))


if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    min_max_sum(arr)
