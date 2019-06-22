

def f(word):
    '''
    Recall that if c is an ascii character then ord(c) returns its ascii code.
    Will be tested on nonempty strings of lowercase letters only.

    >>> f('x')
    The longest substring of consecutive letters has a length of 1.
    The leftmost such substring is x.
    >>> f('xy')
    The longest substring of consecutive letters has a length of 2.
    The leftmost such substring is xy.
    >>> f('ababcuvwaba')
    The longest substring of consecutive letters has a length of 3.
    The leftmost such substring is abc.
    >>> f('abbcedffghiefghiaaabbcdefgg')
    The longest substring of consecutive letters has a length of 6.
    The leftmost such substring is bcdefg.
    >>> f('abcabccdefcdefghacdef')
    The longest substring of consecutive letters has a length of 6.
    The leftmost such substring is cdefgh.
    '''
    desired_length = 0
    desired_substring = ''
    # Insert your code here
    one_str = word[0]
    # L = []
    _max_str = ''
    for i in range(len(word) - 1):
        if ord(word[i + 1]) == ord(one_str[-1]) + 1:
            one_str += word[i + 1]
        else:
            if len(_max_str) < len(one_str):
                _max_str = one_str
            # L.append(one_str)
            one_str = word[i + 1]
    if len(_max_str) < len(one_str):
        _max_str = one_str
    # _max_str = max(L, key = lambda x: len(x))
    print(f"The longest substring of consecutive letters has a length of {len(_max_str)}.")
    print(f"The leftmost such substring is {_max_str}.")



if __name__ == '__main__':
    import doctest
    doctest.testmod()
