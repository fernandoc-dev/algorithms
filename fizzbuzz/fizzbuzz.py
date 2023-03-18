"""
Fizz buzz is a group word game for children to teach them about division. Players take turns to count incrementally, replacing any number divisible by three with the word “fizz”, and any number divisible by five with the word “buzz”.

Our goal is to test a starting round of fizz buzz from 1 to 100 as follow:

1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz…
"""

#
# Complete the 'fizzbuzz' function below.
#
# The function is expected to return a list.
# The function accepts INTEGER_LIST LIST as parameter.
#


def fizzbuzz(LIST:list)->list:
    '''
    Evaluate each item in a list to check if it is divisible by 3, by 5 or none.

    In case the item is divisible by 3, it replaces the integer by "fizz",
    in case the item is divisible by 5, it replaces the integer by "buzz",
    in case the item is divisible by neither, it does not replace the number at all.

    Parameters
    ----------
    LIST : list of int
        List of integers values to evaluate if they are devisible by 3 or 5.

    Return
    ------
    fizzbuzz_list: list
        List based on LIST but replacing the divisibles items by 3 and 5 for "fizz" and "buzz".

    Example
    --------
    >>> fizzbuzz([1,2,3,4,5])
    [1, 2, 'fizz', 4, 'buzz']
    '''
    fizzbuzz_list=list()
    for i in LIST:
        if i % 3 == 0:
            fizzbuzz_list.append("fizz")
        elif i % 5 == 0:
            fizzbuzz_list.append("buzz")
        else:
            fizzbuzz_list.append(i)    
    return fizzbuzz_list    

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    LIST = [1,3,7,77,5,2,5,25,15,9,97]
    print(fizzbuzz(LIST))
