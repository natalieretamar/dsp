# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def donuts(count):
    if count >= 10:
        print 'Number of donuts: many'
    else:
        print 'Number of donuts: %d' %(count)
   
 """
    Given an int count of a number of donuts, return a string of the
    form 'Number of donuts: <count>', where <count> is the number
    passed in. However, if the count is 10 or more, then use the word
    'many' instead of the actual count.

    >>> donuts(4)
    'Number of donuts: 4'
    >>> donuts(9)
    'Number of donuts: 9'
    >>> donuts(10)
    'Number of donuts: many'
    >>> donuts(99)
    'Number of donuts: many'
    """
    raise NotImplementedError


def both_ends(s):
    temp = []
    if len(s) < 2:
        return temp
    else:
        temp.append(s[:2])
        temp.append(s[-2])
        temp.append(s[-1])
        temp= ''.join(temp)
        print temp
        return temp

    """
    Given a string s, return a string made of the first 2 and the last
    2 chars of the original string, so 'spring' yields 'spng'.
    However, if the string length is less than 2, return instead the
    empty string.

    >>> both_ends('spring')
    'spng'
    >>> both_ends('Hello')
    'Helo'
    >>> both_ends('a')
    ''
    >>> both_ends('xyz')
    'xyyz'
    """
    raise NotImplementedError


def fix_start(s):
    #holds value of first letter in string
    tracker= s[0]
    for x in s:
        s = s.replace(tracker, '*')#replace occurances of first letter
        temp = list(s) #break up string
        temp[0]= tracker #re-assign 1st letter
        s = ''.join(temp) #convert to single string
    print s
    return s


    """
    Given a string s, return a string where all occurences of its
    first char have been changed to '*', except do not change the
    first char itself. e.g. 'babble' yields 'ba**le' Assume that the
    string is length 1 or more.

    >>> fix_start('babble')
    'ba**le'
    >>> fix_start('aardvark')
    'a*rdv*rk'
    >>> fix_start('google')
    'goo*le'
    >>> fix_start('donut')
    'donut'
    """
    raise NotImplementedError


def mix_up(a, b):
    a=list(a)
    b=list(b)
    temp_a = a[0:2]

    for i in range(2):
        a[i] = b[i]
        b[i] = temp_a[i]

    a = ''.join(a)
    b = ''.join(b)
    new_string = a+ ' ' + b
    print new_string
    return new_string



    """
    Given strings a and b, return a single string with a and b
    separated by a space '<a> <b>', except swap the first 2 chars of
    each string. Assume a and b are length 2 or more.

    >>> mix_up('mix', 'pod')
    'pox mid'
    >>> mix_up('dog', 'dinner')
    'dig donner'
    >>> mix_up('gnash', 'sport')
    'spash gnort'
    >>> mix_up('pezzy', 'firm')
    'fizzy perm'
    """
    raise NotImplementedError


def verbing(s):
    if len(s) >=3:
        if s[-3] != 'i' and s[-2] != 'n' and s[-1] != 'g':
            s = s + 'ing'
            print s
            return s
        elif s[-3] == 'i' and s[-2] == 'n' and s[-1] == 'g':
            s = s + 'ly'
            print s
            return s
    else:
        print s
        return s


"""
    Given a string, if its length is at least 3, add 'ing' to its end.
    Unless it already ends in 'ing', in which case add 'ly' instead.
    If the string length is less than 3, leave it unchanged. Return
    the resulting string.

    >>> verbing('hail')
    'hailing'
    >>> verbing('swiming')
    'swimingly'
    >>> verbing('do')
    'do'
    """
    raise NotImplementedError


def not_bad(s):
    delimiter = ' '
    s = s.split(delimiter)
    if 'not' in s and 'bad' in s:
        tracker1 = s.index('not')
        tracker2 = s.index('bad')
        if tracker2 > tracker1:
            del s[tracker1 : (len(s)+1)]
            s.append('good')

    s = ' '.join(s)
    print s
    return s


    """
    Given a string, find the first appearance of the substring 'not'
    and 'bad'. If the 'bad' follows the 'not', replace the whole
    'not'...'bad' substring with 'good'. Return the resulting string.
    So 'This dinner is not that bad!' yields: 'This dinner is
    good!'

    >>> not_bad('This movie is not so bad')
    'This movie is good'
    >>> not_bad('This dinner is not that bad!')
    'This dinner is good!'
    >>> not_bad('This tea is not hot')
    'This tea is not hot'
    >>> not_bad("It's bad yet not")
    "It's bad yet not"
    """
    raise NotImplementedError


def front_back(a, b):

    #a variables
    a_temp = list(a)
    a_front = []
    a_back=[]

    #index is list holding result of div and remainder
    a_index = divmod(len(a),2)
    #if there is no remainder-list is even
    if a_index[1] == 0:
        a_front = a_temp[0:a_index[0]]
        a_back = a_temp[a_index[0] : len(a)]
    else:
        a_front = a_temp[0:a_index[0]+1]
        a_back = a_temp[a_index[0]+1 : len(a)]

    a_front = ''.join(a_front)
    a_back = ''.join(a_back)

    #b variables
    b_temp = list(b)
    b_front = []
    b_back= []

    b_index = divmod(len(b),2)
    if b_index[1] == 0:
        b_front = b_temp[0:b_index[0]]
        b_back = b_temp[b_index[0] : len(b)]
    else:
        b_front = b_temp[0:b_index[0]+1]
        b_back = b_temp[b_index[0]+1 : len(b)]

    b_front = ''.join(b_front)
    b_back = ''.join(b_back)

    new_string = a_front + b_front + a_back + b_back
    print new_string
    return new_string



    """
    Consider dividing a string into two halves. If the length is even,
    the front and back halves are the same length. If the length is
    odd, we'll say that the extra char goes in the front half. e.g.
    'abcde', the front half is 'abc', the back half 'de'. Given 2
    strings, a and b, return a string of the form a-front + b-front +
    a-back + b-back

    >>> front_back('abcd', 'xy')
    'abxcdy'
    >>> front_back('abcde', 'xyz')
    'abcxydez'
    >>> front_back('Kitten', 'Donut')
    'KitDontenut'
    """
    raise NotImplementedError
