"""
Statement: Create a function that is capable of detecting and returning all
handles a text using only Regular Expressions.
You must create a regular expression for each case:
- Handle user: Those that begin with "@"
- Handle hashtag: Those that begin with "#"
- Handle web: Those that begin with "www.", "http://", "https://"
and end with a domain (.com, .es...)
"""
import re

def extract_users_hashtag_web(text)->list:
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
    >>> extract_users_hashtag_web('The users @peter and @jhon are working on www.projects.com and https://google.com about #testing')
    [['@peter', '@jhon'], ['#testing'], ['www.projects.com', 'https://google.com']]
    '''
    users = re.findall("@[^\s]*", text)
    hashtags=re.findall("#[^\s]*", text)
    webs=re.findall("[www.|http://|https://][^\s]*[.][^\s]*", text)
    result=list()
    result.append(users)
    result.append(hashtags)
    result.append(webs)
    print(result)

extract_users_hashtag_web('The users @peter and @jhon are working on www.projects.com and https://google.com about #testing')

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    
