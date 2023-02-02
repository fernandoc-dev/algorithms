"""
Given a square matrix, calculate the absolute difference between the sums of its diagonals.

For example, the square matrix arr is shown below:
1 2 3
4 5 6
9 8 9

The left-to-right diagonal 1 + 5 + 9 = 15. The right to left diagonal 3 + 5 + 9 = 17.
Their absolute difference is 2.
"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonal_difference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#


def diagonal_difference(arr:list)->int:
    '''
    Calc the absolute difference.

    Cal the sum of diagonal elements from left to right (sum1),
    Cal the sum of diagonal elements from right to left (sum2),
    Cal the absolute difference sum1-sum2.

    Parameters
    ----------
    arr : list of int
        Square List of integers.

    Return
    ------
    abs_diff: int.

    Examples
    --------
    arr = [[1, 3, 6], [4, 1, 7], [7, 3, 6]]
    abs_diff = 6
    
    arr = [[1, 3, 6, 3], [4, 1, 7, 3], [7, 3, 6, 4], [8, 2, 5, 3]]
    abs_diff = 10
    '''
    sum1 = 0
    sum2 = 0
    for i in range(N):
        sum1 += arr[i][i]
        sum2 += arr[i][N-i-1]
    abs_diff=abs(sum1-sum2)
    return abs_diff


if __name__ == '__main__':

    N = 4

    source = [[1, 3, 6, 3], [4, 1, 7, 3], [7, 3, 6, 4], [8, 2, 5, 3]]
    x = diagonal_difference(source)
    print(x)
