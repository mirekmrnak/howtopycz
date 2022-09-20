def is_divisible(m,n):
    """
    >>> is_divisible(20,4)
    True
    >>> is_divisible(21,8)
    False
    """
    return m % n == 0

if __name__ == '__main__':
    import doctest
    doctest.testmod()