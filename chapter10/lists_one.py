def make_empty(seq):
    """
    >>> make_empty([1, 2, 3, 4])
    []
    >>> make_empty(('a', 'b', 'c'))
    ()
    >>> make_empty("No, not me!")
    ''
    """
    return seq[0:0]

def insert_at_end(val, seq):
    """
    >>> insert_at_end(5, [1, 3, 4, 6])
    [1, 3, 4, 6, 5]
    >>> insert_at_end('x', 'abc')
    'abcx'
    >>> insert_at_end(5, (1, 3, 4, 6))
    (1, 3, 4, 6, 5)
    """
    if type(seq) == type(""):
        return seq + val
    if type(seq) == type([]):
        return [*seq, val]
    if type(seq) == type((1,2)):
        return (*seq, val)

def insert_in_front(val, seq):
    """
    >>> insert_in_front(5, [1, 3, 4, 6])
    [5, 1, 3, 4, 6]
    >>> insert_in_front(5, (1, 3, 4, 6))
    (5, 1, 3, 4, 6)
    >>> insert_in_front('x', 'abc')
    'xabc'
    """
    if type(seq) == type(""):
        return val + seq
    if type(seq) == type([]):
        return [val, *seq]
    if type(seq) == type((1,2)):
        return (val, *seq)

def index_of(val, seq, start=0):
    """
    >>> index_of(9, [1, 7, 11, 9, 10])
    3
    >>> index_of(5, (1, 2, 4, 5, 6, 10, 5, 5))
    3
    >>> index_of(5, (1, 2, 4, 5, 6, 10, 5, 5), 4)
    6
    >>> index_of('y', 'happy birthday')
    4
    >>> index_of('banana', ['apple', 'banana', 'cherry', 'date'])
    1
    >>> index_of(5, [2, 3, 4])
    -1
    >>> index_of('b', ['apple', 'banana', 'cherry', 'date'])
    -1
    """
    if val in seq:
        return seq.index(val, start)
    else:
        return -1

def remove_at(index, seq):
    """
    >>> remove_at(3, [1, 7, 11, 9, 10])
    [1, 7, 11, 10]
    >>> remove_at(5, (1, 4, 6, 7, 0, 9, 3, 5))
    (1, 4, 6, 7, 0, 3, 5)
    >>> remove_at(2, "Yomrktown")
    'Yorktown'
    """
    return seq[:index]+seq[index+1:]

def remove_val(val, seq):
    """
    >>> remove_val(11, [1, 7, 11, 9, 10])
    [1, 7, 9, 10]
    >>> remove_val(15, (1, 15, 11, 4, 9))
    (1, 11, 4, 9)
    >>> remove_val('what', ('who', 'what', 'when', 'where', 'why', 'how'))
    ('who', 'when', 'where', 'why', 'how')
    """
    if type(seq) == type([]):
        new_lst = seq.copy()
        new_lst.remove(val)
        return new_lst
    if type(seq) == type((1,2)):
        new_lst = list(seq)
        new_lst.remove(val)
        return tuple(new_lst)

def remove_all(val, seq):
    """
    >>> remove_all(11, [1, 7, 11, 9, 11, 10, 2, 11])
    [1, 7, 9, 10, 2]
    >>> remove_all('i', 'Mississippi')
    'Msssspp'
    """
    new_seq = []
    for i in seq:
        if i != val:
            new_seq.append(i)
    if type(seq) == type([]):
        return new_seq
    if type(seq) == type(''):
        return ''.join(new_seq)
    if type(seq) == type((1,2)):
        return tuple(new_seq)

def count(val, seq):
    """
    >>> count(5, (1, 5, 3, 7, 5, 8, 5))
    3
    >>> count('s', 'Mississippi')
    4
    >>> count((1, 2), [1, 5, (1, 2), 7, (1, 2), 8, 5])
    2
    """
    return seq.count(val)

def reverse(seq):
    """
    >>> reverse([1, 2, 3, 4, 5])
    [5, 4, 3, 2, 1]
    >>> reverse(('shoe', 'my', 'buckle', 2, 1))
    (1, 2, 'buckle', 'my', 'shoe')
    >>> reverse('Python')
    'nohtyP'
    """
    return seq[::-1]

def sort_sequence(seq):
    """
    >>> sort_sequence([3, 4, 6, 7, 8, 2])
    [2, 3, 4, 6, 7, 8]
    >>> sort_sequence((3, 4, 6, 7, 8, 2))
    (2, 3, 4, 6, 7, 8)
    >>> sort_sequence("nothappy")
    'ahnoppty'
    """
    new_seq = list(seq)
    new_seq.sort()
    if type(seq) == type([]):
        return new_seq
    if type(seq) == type(''):
        return ''.join(new_seq)
    if type(seq) == type((1,2)):
        return tuple(new_seq)

if __name__ == "__main__":
    import doctest
    doctest.testmod()