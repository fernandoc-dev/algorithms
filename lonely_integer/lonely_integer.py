"""
Given an array of integers, where all elements but one occur twice, find the unique element.

Example

a=[1,2,3,4,3,2,1]

The unique element is 4.

Function Description

Complete the lonely_integer function in the editor below.

lonely_integer has the following parameter(s):

values: an array of integers

Returns

int: the element that occurs only once

Input Format

The first line contains a single integer, N, the number of integers in the array.
The second line contains n space-separated integers that describe the values in a.

Constraints

1) N>=1, N<100

2) N is an odd number

3) a[i]>=0, a[i]<=100

It is guaranteed that there is one unique element.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonely_integer' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#


def lonely_integer(values:list)->int:
    '''
    Find the one unique element.

    Find one unique element between n repeated elements.

    Parameters
    ----------
    values : list of int
        len(values) is an odd number.

    Return
    ------
    i: int.

    Examples
    --------
    values = [1,2,3,2,1]
    i = 3.

    values = [2,2,1,1,3]
    i = 3.
    '''
    if (len(values)<1 and len(values)>=100):
        raise ValueError('Values must contain odd number of elements')
    if len(values) % 2 == 0:
        raise ValueError('Odd number of elements is required')
    for i in values:
        if (i>0 and i<=100):
            if values.count(i) == 1:
                return i
        else: raise ValueError('Values out of range:')


if __name__ == '__main__':

    A=[1,2,3,2,1]

    result = lonely_integer(A)

    print(result)
