# Podle naznačených výsledků sestavte možnou hodnotu seznamu a_list:
"""
   >>> a_list[3]
   42
   >>> a_list[6]
   'Ni!'
   >>> len(a_list)
   8
"""
a_list = [0, 0, 0, 42, 0, 0, 'Ni!', 0]

# Podle naznačených výsledků sestavte možnou hodnotu seznamu b_list a c_list:
"""
   >>> b_list[1:]
   ['Stills', 'Nash']
   >>> group = b_list + c_list
   >>> group[-1]
   'Young'
"""
b_list = [0, 'Stills', 'Nash']
c_list = ['Young']

# Podle naznačených výsledků sestavte možnou hodnotu seznamu mystery_list:
"""
   >>> 'war' in mystery_list
   False
   >>> 'peace' in mystery_list
   True
   >>> 'justice' in mystery_list
   True
   >>> 'oppression' in mystery_list
   False
   >>> 'equality' in mystery_list
   True
"""
mystery_list = ['peace', 'justice', 'equality']

# Vytvořte funkci list_range s naznačeným výstupem:
"""
   >>> list_range(a, b, c)
   [5,9,13,17]
"""
def list_range(a, b, c=1):
    """
    count = a
    end = b
    lst = [count]
    while count < b:
        count += c
        lst.append(count)
    return lst
    """
    return [x for x in range(a, b+1, c)]   

if __name__ == '__main__':
    import doctest
    doctest.testmod()