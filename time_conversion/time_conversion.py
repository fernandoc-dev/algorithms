"""
Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

Sample Input
07:05:45PM

Sample Output
19:05:45
"""
#
# Complete the 'time_conversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def time_conversion(time12:str)->str:
    '''
    Convert from format 12H to format 24H.

    Take the string with the structure '07:05:45PM' and
    return a string with the structure '19:05:45'

    Parameters
    ----------
    time12 : str
        Time in 12H format.

    Return
    ------
    time24:str.
        Time in 24H format.

    Examples
    --------
    input '07:05:45PM'
    output '19:05:45'
    
    input '12:05:45AM'
    output '00:05:45'
    '''
    time24=time12[:-2]
    if time12[-2:] == 'PM' and time12[:2] != '12':
        time24 = str(int(time12[:2])+12)+time12[2:-2]
    elif time12[-2:] == 'AM' and time12[:2]== '12':
        time24 = '00'+ time12[2:-2]

    return time24


if __name__ == '__main__':

    s = '07:05:45PM'

    result = time_conversion(s)

    print(result)
