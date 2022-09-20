def is_multiple(m,n):
    """
    >>> is_multiple(12,3)
    True
    >>> is_multiple(12,4)
    True
    >>> is_multiple(12,5)
    False
    """
    return m % n == 0

if __name__ == '__main__':
    import doctest
    doctest.testmod()