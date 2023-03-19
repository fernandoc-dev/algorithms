"""
Statement: Create a function that receives a text and returns the vowel that
more times to be repeated.
- If there are no vowels, it can return empty.
"""

def frequency_vocal(text)->str:
    '''
    Extract from a given text the Handle user, Handle hastag and Handle web

    Parameters
    ----------
    text : string
        Text to find the handles.

    Return
    ------
    result: list
        List that contain all handles extracted.

    Example
    --------
    >>> frequency_vocal('The users @peter and @jhon are working on www.projects.com and https://google.com about #testing')
    'o'
    '''
    text=text.lower()
    result=""
    vocals=['a','e','i','o','u']
    frequency=list()
    frequency.append(text.count('a'))
    frequency.append(text.count('e'))
    frequency.append(text.count('i'))
    frequency.append(text.count('o'))
    frequency.append(text.count('u'))
    for i in range(0,5):
        if frequency[i]==max(frequency):
            if result!="":
                result+=", " + vocals[i]
            else:
                result=vocals[i]
    return result

print(frequency_vocal('The users @peter and @jhon are working on www.projects.com and https://google.com about #testing'))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    
