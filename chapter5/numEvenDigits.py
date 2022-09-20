def num_even_digits(n): 
    """
    >>> num_even_digits(123456)
    3
    >>> num_even_digits(2468)
    4
    >>> num_even_digits(1357)
    0
    >>> num_even_digits(2)
    1
    >>> num_even_digits(20)
    2
    """
    evens = [number for number in str(n) if int(number) % 2 == 0] #list komprehenze
    return len(evens)


if __name__ == '__main__':
    import doctest
    doctest.testmod()