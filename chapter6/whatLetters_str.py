def count_letter_acc(strng, ch):
    """
    Fce přijímá řetězec a písmeno jako argument a vrací počet výskytů písmena v řetězci.
    >>> count_letter_acc("Měla babka čtyři jabka", "a")
    5
    >>> count_letter_acc("Honolulu", "o")
    2
    >>> count_letter_acc("Ahoj", "z")
    0
    """
    count = 0
    for char in strng:
        if char == ch:
            count = count + 1
    return count

print("Honolulu".count("o")) #řešeno str metodou count

if __name__ == '__main__':
    import doctest
    doctest.testmod()