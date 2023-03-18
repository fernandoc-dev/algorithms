"""
Write a function that takes two words (Strings) and returns
true or false (Bool) depending on whether they are anagrams or not.
An Anagram is formed by rearranging ALL the letters of one initial word.
It is NOT necessary to check that both words exist.
Two exactly identical words are not an anagram.
"""
def anagram(word_1,word_2):
    '''
    Compare 2 words and determine if they are anagrams.

    Parameters
    ----------
    word_1 : string
    word_2 : string

    Return
    ------
    anagram: boolean
        The result of testing if string_1 and string_2 are anagrams

    Example
    --------
    >>> anagram('calipso','ospilac')
    True

    >>> anagram('calipso','calipso')
    False

    >>> anagram('CalipSo','calipso')
    False

    >>> anagram('CalipSo','ospilac')
    True
    '''
    if word_1.lower()==word_2.lower():
        return False
    if sorted([*word_1.lower()])==sorted([*word_2.lower()]):
        return True
    return False

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    
    print(anagram('CaliPso','ospilac'))
