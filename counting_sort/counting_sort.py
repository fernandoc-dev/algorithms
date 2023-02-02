"""
Comparison Sorting
Quicksort usually has a running time of n x log(n), but is there an algorithm that can sort even faster? In general, this is not possible. Most sorting algorithms are comparison sorts, i.e. they sort a list just by comparing the elements to one another. A comparison sort algorithm cannot beat n x log(n) (worst-case) running time, since n x log(n) represents the minimum number of comparisons needed to know where to place each element.

Alternative Sorting
Another sorting method, the counting sort, does not require comparison. Instead, you create an integer array whose index range covers the entire range of values in your array to sort. Each time a value occurs in the original array, you increment the counter at that index. At the end, run through your counting array, printing the value of each non-zero valued index that number of times.

Example

arr=[1,1,3,2,1]

i	arr[i]	result
0	1	[0, 1, 0, 0]
1	1	[0, 2, 0, 0]
2	3	[0, 2, 0, 1]
3	2	[0, 2, 1, 1]
4	1	[0, 3, 1, 1]

Note
For this exercise, always return a frequency array with 100 elements. The example above shows only the first 4 elements, the remainder being zeros.

Challenge
Given a list of integers, count and return the number of times each value appears as an array of integers.

Function Description

Complete the counting_sort function in the editor below.

counting_sort has the following parameter(s):

arr[n]: an array of integers

Returns

int[100]: a frequency array

Constrains
20 <= n < 10^6
0 <= arr[i] < 100
"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'counting_sort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def counting_sort(list_int:list)->list:
    '''
    Sort a list of integers counting the frecuence but not comparating values.

    This function creates a list whose size is used for representing each possible
    value as an index, and each value in the list represents the frequency each value appears.

    Parameters
    ----------
    list_int : list of int
        List of integers values to sort.

    Return
    ------
    frecuency_array: list of int
        List whose each index represents a value in list int and the values
        in frecuency_array represents the frequency of those list_int's values.

    Examples
    --------
    arr=[1,1,3,2,1]
    frecuency_array=[0,3,1,1]

    arr=[0,3,3,2,0]
    frecuency_array=[2,0,1,2]
    '''
    if 20 <= N <= 10**6:  # First constrain
        frecuency_array = []
        for i in range(max(list_int)+1):
            frecuency_array.append(list_int.count(i))
            if len(list_int) > i:
                if list_int[i] < 0 >= 100:  # Second constrain
                    raise ValueError('Second constrain violated')
    else:
        raise ValueError('First constrain violated')
    return frecuency_array


if __name__ == '__main__':

    N = 20
    VALUES = '3 19 15 1 2 2 5 25 3 1 1 0 8 19 12 0 1 3 14 19'
    arr = list(map(int, VALUES.rstrip().split()))

    result = counting_sort(arr)
    print('Array of frequencies:')
    print(result)

    matrix=[]
    for x in range(len(result))[::-1]:  # Loop inverse on result
        if result[x]:                   # If the value appeard at least once
            for y in range(result[x]):  # Insert the value into the array as
                                        # many times as it has appeared in the original array
                matrix.append(x)
    print('Sorted List:')
    print(matrix)
