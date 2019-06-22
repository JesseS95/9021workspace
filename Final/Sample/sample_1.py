
def remove_consecutive_duplicates(word):
    '''
    >>> remove_consecutive_duplicates('')
    ''
    >>> remove_consecutive_duplicates('a')
    'a'
    >>> remove_consecutive_duplicates('ab')
    'ab'
    >>> remove_consecutive_duplicates('aba')
    'aba'
    >>> remove_consecutive_duplicates('aaabbbbbaaa')
    'aba'
    >>> remove_consecutive_duplicates('abcaaabbbcccabc')
    'abcabcabc'
    >>> remove_consecutive_duplicates('aaabbbbbaaacaacdddd')
    'abacacd'
    '''
    # Insert your code here (the output is returned, not printed out)

    # output = ''
    # for i in range(len(word)):
    #     if output == '':
    #         output += word[i]
    #     elif output[-1] != word[i]:
    #         output += word[i]
    # return output
    output = ''
    for i in range(len(word)):
        if output =='':
            output +=word[i]
        elif output[-1] != word[i]:
            output += word[i]
    return output






if __name__ == '__main__':
    import doctest
    doctest.testmod()
