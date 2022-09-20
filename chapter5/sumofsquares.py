def sum_of_squares(n): 
    """
    >>> sum_of_squares(1)
    1
    >>> sum_of_squares(9)
    81
    >>> sum_of_squares(11)
    2
    >>> sum_of_squares(121)
    6
    >>> sum_of_squares(987)
    194
    """
    it = (int(number)**2 for number in str(n)) #generator
    return sum(it)

if __name__ == '__main__':
    import doctest
    doctest.testmod()