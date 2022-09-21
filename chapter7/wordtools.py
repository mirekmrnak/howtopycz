import string

def cleanword(word):
    """
    >>> cleanword('what?')
    'what'
    >>> cleanword('"now!"')
    'now'
    >>> cleanword('?+="word!,@$()"')
    'word'
    """
    cleanword = ''
    for ch in word:
        if ch not in string.punctuation:
            cleanword += ch
    return cleanword

def has_dashdash(s):
    """
    >>> has_dashdash('distance--but')
    True
    >>> has_dashdash('several')
    False
    >>> has_dashdash('critters')
    False
    >>> has_dashdash('spoke--fancy')
    True
    >>> has_dashdash('yo-yo')
    False
    """
    return '--' in s

def extract_words(s):
    """
    >>> extract_words('Now is the time!"Now", is the time? Yes, now.')
    ['now', 'is', 'the', 'time', 'now', 'is', 'the', 'time', 'yes', 'now']
    >>> extract_words('she tried to curtsey as she spoke--fancy')
    ['she', 'tried', 'to', 'curtsey', 'as', 'she', 'spoke', 'fancy']
    """
    no_punc = ""
    for ch in s:
        if ch not in string.punctuation:
            no_punc += ch
        else:
            no_punc += ' '
    
    no_punc = no_punc.lower()
    return no_punc.split()

def wordcount(word, wordlist):
    """
    >>> wordcount('now', ['now', 'is', 'time', 'is', 'now', 'is', 'is'])
    ['now', 2]
    >>> wordcount('is', ['now', 'is', 'time', 'is', 'now', 'is', 'the', 'is'])
    ['is', 4]
    >>> wordcount('time', ['now', 'is', 'time', 'is', 'now', 'is', 'is'])
    ['time', 1]
    >>> wordcount('frog', ['now', 'is', 'time', 'is', 'now', 'is', 'is'])
    ['frog', 0]
    """
    return [word, wordlist.count(word)]

def wordset(wordlist):
    """
    >>> wordset(['now', 'is', 'time', 'is', 'now', 'is', 'is'])
    ['is', 'now', 'time']
    >>> wordset(['I', 'a', 'a', 'is', 'a', 'is', 'I', 'am'])
    ['I', 'a', 'am', 'is']
    >>> wordset(['or', 'a', 'am', 'is', 'are', 'be', 'but', 'am'])
    ['a', 'am', 'are', 'be', 'but', 'is', 'or']
    """
    return sorted(list(set(wordlist)))

def longestword(wordset):
    """
    >>> longestword(['a', 'apple', 'pear', 'grape'])
    5
    >>> longestword(['a', 'am', 'I', 'be'])
    2
    >>> longestword(['this', 'that', 'supercalifragilisticexpialidocious'])
    34
    """
    longestword = 0
    for word in wordset:
        if len(word) > longestword:
            longestword = len(word)
    
    return longestword

if __name__ == '__main__':
    import doctest
    doctest.testmod()