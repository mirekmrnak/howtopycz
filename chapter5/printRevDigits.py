def print_digits(n): 
    """
    >>> print_digits(13789)
    '9 8 7 3 1'
    >>> print_digits(39874613)
    '3 1 6 4 7 8 9 3'
    >>> print_digits(213141)
    '1 4 1 3 1 2'
    """
    new_string = ''
    for number in str(n):
        new_string = number + ' ' + new_string
    return new_string.rstrip()

if __name__ == '__main__':
    import doctest
    doctest.testmod()