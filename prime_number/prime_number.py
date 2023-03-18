"""
Write a program that checks whether or not a number is prime.
Once this is done, print the prime numbers between 1 and 100.
"""
def identify_prime(number):
    """
    Tests:
    >>> identify_prime(5)
    True
    >>> identify_prime(6)
    False
    """
    prime=True
    for j in range(2,number):
        if number%j==0 and number!=j:
            prime=False
    if prime==True:
        return True
    return False
    
def print_prime_numbers():
    prime_numbers=list()
    for i in range(2,101):
        if identify_prime(i):
            prime_numbers.append(i)
    return(prime_numbers)
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()

print(identify_prime(5))
print(print_prime_numbers())
    
