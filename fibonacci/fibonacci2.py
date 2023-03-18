"""
 Write a program that prints the first 50 numbers of the sequence
 of Fibonacci starting at 0.
 - The Fibonacci series is made up of a sequence of numbers in
 the one that the next is always the sum of the two previous ones.
 0, 1, 1, 2, 3, 5, 8, 13...
"""

def fibonacci():
    '''
    Print the first 50 numbers of the sequence of Fibonacci starting at 0.
    '''
    penultimate=0
    last=1
    fibonacci=1
    for i in range (0,50):
        print(penultimate)
        penultimate=last
        last=fibonacci
        fibonacci=penultimate+last

fibonacci()