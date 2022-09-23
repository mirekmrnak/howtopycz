# Napište fci is_divisible(num,f), která přijme celá čísla jako argument a podle situace vytiskne "Toto číslo je dělitelné číslem f" nebo "Toto číslo neni dělitelné číslem f".
def is_divisible(num,f):
    '''
    >>> is_divisible(20,4)
    'Toto číslo je dělitelné číslem 4'
    >>> is_divisible(21,8)
    'Toto číslo neni dělitelné číslem 8'
    '''
    return f'Toto číslo je dělitelné číslem {f}' if num % f == 0 else f'Toto číslo neni dělitelné číslem {f}'

if __name__ == '__main__':
    import doctest
    doctest.testmod()