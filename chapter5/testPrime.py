def testprime(n):
    """
    >>> testprime(4)
    False
    >>> testprime(5)
    True
    >>> testprime(7)
    True
    >>> testprime(13)
    True
    """
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

def print_primes(n):
    #Vytiskne prvních n prvočísel
    for i in range(1, n+1):
        if testprime(i):
            print(i, '\t', end="")
    print()

if __name__ == '__main__':
    import doctest
    doctest.testmod()