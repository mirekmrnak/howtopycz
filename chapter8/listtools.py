# Napište funkci add_lists(a,b) která přijme dva seznamy stejné délky s celými čísly a vrátí nový seznam se součty odpovídajících položek.

def add_lists(a, b):
    """
    >>> add_lists([1,1], [1,1])     
    [2, 2]
    >>> add_lists([1,2], [1,4])     
    [2, 6]
    >>> add_lists([1,2,1], [1,4,3])     
    [2, 6, 4]
    """
    return [a[i]+b[i] for i in range(len(a))]

# Napište funkci mult_lists(a, b) která přijme dva seznamy stejné délky s celými čísly a vrátí součet součinů odpovídajících položek.

def mult_lists(a, b):
    """
    >>> mult_lists([1,1], [1,1])     
    2
    >>> mult_lists([1,2], [1,4])     
    9
    >>> mult_lists([1,2,1], [1,4,3])     
    12
    """
    return sum(a[i]*b[i] for i in range(len(a)))

nums = [1, 2, 3, 4]
print([(x, y) for x in nums for y in nums if x != y])

lst = []
for x in nums:
    for y in nums:
        if x != y:
            lst.append((x, y))
print(lst)

if __name__ == '__main__':
    import doctest
    doctest.testmod()