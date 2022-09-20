def hypotenuse (a,b):
    """
    >>> hypotenuse(3,4)
    5.0
    >>> hypotenuse(12,5)
    13.0
    >>> hypotenuse(7,24)
    25.0
    """
    # tělo funkce může mít pouhé 2 řádky
    from math import sqrt
    return sqrt(a**2 + b**2)

if __name__ == '__main__':
    import doctest
    doctest.testmod()