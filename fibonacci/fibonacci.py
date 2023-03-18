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
    last=0
    penultimate=0
    for i in range (0,50):
        if i==0 or i==1:
            print(i)
            last=1
        else:
            print(last+penultimate)
            i=last
            last=last+penultimate
            penultimate=i
        
fibonacci()