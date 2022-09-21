def reverse (s):
   """
   >>> reverse('happy')
   'yppah'
   >>> reverse('Python') 
   'nohtyP'
   >>> reverse('')
   ''
   >>> reverse('P')
   'P'
   """
   print("'" + s[::-1] + "'")

def mirror (s):
    """
    >>> mirror ('good')
    'gooddoog'
    >>> mirror ('yes') 
    'yessey'
    >>> mirror ('Python')
    'PythonnohtyP'
    >>> mirror ('')
    ''
    >>> mirror ('a')
    'aa'
    """
    print("'" + s + s[::-1] + "'")

def is_palindrome (s):
    """
    >>> is_palindrome('abba')
    True
    >>> is_palindrome('abab') 
    False
    >>> is_palindrome('tenet')
    True
    >>> is_palindrome('banana')
    False
    >>> is_palindrome('straw warts')
    True
    """
    return s == s[::-1]

def remove_letter (ch, strng):
    """
    >>> remove_letter ('a', 'apple')
    'pple'
    >>> remove_letter ('a', 'banana') 
    'bnn'
    >>> remove_letter ('z', 'banana')
    'banana'
    >>> remove_letter ('i', 'Mississippi')
    'Msssspp'
    """
    print("'" + strng.replace(ch, '') + "'")

def count_sub (sub, s):
    """
    >>> count_sub('is', 'Mississippi')
    2
    >>> count_sub('an', 'banana') 
    2
    >>> count_sub('ana', 'banana')
    2
    >>> count_sub('nana', 'banana')
    1
    >>> count_sub('nanan', 'banana')
    0
    """
    count = 0
    for i in range(len(s)-len(sub)+1):
        if (s[i:i+len(sub)]) == sub:
            count += 1
    return count

def remove_sub (sub, s):
    """
    >>> remove_sub('an', 'banana') 
    'bana'
    >>> remove_sub('cyc', 'bicycle')
    'bile'
    >>> remove_sub('iss', 'Mississippi')
    'Missippi'
    >>> remove_sub('egg', 'bicycle')
    'bicycle'
    """
    return s.replace(sub, '', 1)

def remove_all (sub, s):
    """
    >>> remove_all('an', 'banana') 
    'ba'
    >>> remove_all('cyc', 'bicycle')
    'bile'
    >>> remove_all('iss', 'Mississippi')
    'Mippi'
    >>> remove_all('egg', 'bicycle')
    'bicycle'
    """
    return s.replace(sub, '')

if __name__ == '__main__':
    import doctest
    doctest.testmod()