def fah2cel(t):
    """
    >>> fah2cel(212)
    100
    >>> fah2cel(32)
    0
    >>> fah2cel(-40)
    -40
    >>> fah2cel(37)
    3
    """
    cel = (t - 32) * 0.5556
    return round(cel, None)

if __name__ == '__main__':
    import doctest
    doctest.testmod()