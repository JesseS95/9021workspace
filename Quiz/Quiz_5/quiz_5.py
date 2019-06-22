# Prompts the user for a nonnegative integer that codes a set S as follows:
# - Bit 0 codes 0
# - Bit 1 codes -1
# - Bit 2 codes 1
# - Bit 3 codes -2
# - Bit 4 codes 2
# - Bit 5 codes -3
# - Bit 6 codes 3
# ...
# Computes a derived nonnegative number that codes the set of running sums
# of the members of S when those are listed in increasing order.
#
# Computes the ordered list of members of a coded set.
#
# Written by ZH Sheng and Eric Martin for COMP9021


import sys

try:
    encoded_set = int(input('Input a nonnegative integer: '))
    if encoded_set < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
        
def display(L):
    print('{', end = '')
    print(', '.join(str(e) for e in L), end = '')
    print('}')

def decode(encoded_set):
    zheng_cat = []
    fu_cat = []
    l_cat = []
    cat = bin(encoded_set)
    cat_length = len(cat) - 2
    panding_cat_length =int( cat_length // 2 )
    for i in range(panding_cat_length,0,-1):
        zheng_cat.append(i)
    for i in range( - panding_cat_length,0,1):
        fu_cat.append(i)
    if cat_length % 2:
        for i in range(panding_cat_length):
            l_cat.append(zheng_cat[i])
            l_cat.append(fu_cat[i])
    else:
        for i in range ( panding_cat_length ):
            l_cat.append(fu_cat[i])
            if i <= len(zheng_cat) - 2:
                l_cat.append(zheng_cat[i+1])
    l_cat.append(int(0))
    if encoded_set == 0:
        l_cat = []
    #print('index = ',l_cat)
    cat_digit = []
    cat_set = []
    for i in range(2,len(cat)):
        cat_digit.append(int(cat[i]))
    #print('digit = ',cat_digit)
    for i in range(len(cat_digit)):
        if cat_digit[i]:
            cat_set.append(l_cat[i])
    cat_set.sort()
    return cat_set

def code_derived_set(encoded_set):
    old_cat = decode(encoded_set)
    dog_number = 0
    if old_cat:
        dog = [old_cat[0]]
        t = old_cat[0]
    else:
        dog = []
        t = 0

    for i in range(1,len(old_cat)):
        t += old_cat[i]
        dog.append(t)
    dog_set = sorted(set(dog))
    for i in dog_set:
        if i < 0:
            dog_number += 2 ** (((- i - 1 ) * 2 ) + 1)
        else:
            dog_number += 2 ** (2 * i)
    return dog_number



print('The encoded set is: ', end = '')
display(decode(encoded_set))
code_of_derived_set = code_derived_set(encoded_set)
print('The derived set is encoded as:', code_of_derived_set)
print('It is: ', end = '')
display(decode(code_of_derived_set))

    
