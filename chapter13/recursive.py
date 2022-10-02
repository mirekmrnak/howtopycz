# funkce recursive_min, která vrátí nejmenší číselnou hodnotu seznamu s vnořenými seznamy.

def recursive_min(nested_num_list):
    """
    >>> recursive_min([2, 9, [1, 13], 8, 6])
    1
    >>> recursive_min([2, [[100, 1], 90], [10, 13], 8, 6])
    1
    >>> recursive_min([2, [[13, -7], 90], [1, 100], 8, 6])
    -7
    >>> recursive_min([[[-13, 7], 90], 2, [1, 100], 8, 6])
    -13
    """
    min_value = nested_num_list[0]
    while type(min_value) == type([]):
        min_value = min_value[0]

    for element in nested_num_list:
        if type(element) != type([]):
            if element < min_value:
                min_value = element
        else:
            if recursive_min(element) < min_value:
                min_value = recursive_min(element)
    
    return min_value

def recursive_count(target, nested_num_list):
    """
    >>> recursive_count(2, [2, 9, [2, 1, 13, 2], 8, [2, 6]])
    4
    >>> recursive_count(7, [[9, [7, 1, 13, 2], 8], [7, 6]])
    2
    >>> recursive_count(15, [[9, [7, 1, 13, 2], 8], [2, 6]])
    0
    >>> recursive_count(5, [[5, [5, [1, 5], 5], 5], [5, 6]])
    6
    """
    count = 0
    for element in nested_num_list:
        if type(element) != type([]):
            if target == element:
                count += 1
        else:
            count += recursive_count(target, element)

    return count    

def flatten(nested_num_list):
    """
    >>> flatten([2, 9, [2, 1, 13, 2], 8, [2, 6]])
    [2, 9, 2, 1, 13, 2, 8, 2, 6]
    >>> flatten([[9, [7, 1, 13, 2], 8], [7, 6]])
    [9, 7, 1, 13, 2, 8, 7, 6]
    >>> flatten([[9, [7, 1, 13, 2], 8], [2, 6]])
    [9, 7, 1, 13, 2, 8, 2, 6]
    >>> flatten([[5, [5, [1, 5], 5], 5], [5, 6]])
    [5, 5, 1, 5, 5, 5, 5, 6]
    """
    new_list = []
    for element in nested_num_list:
        if type(element) == type([]):
            new_list.extend(flatten(element))
        else:
            new_list.append(element)
    
    return new_list

if __name__ == "__main__":
    import doctest
    doctest.testmod()