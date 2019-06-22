# Written by ZH Sheng and Eric Martin for COMP9021
import sys
from random import seed, randint
from math import gcd
try:
    arg_for_seed, length, max_value = input('Enter three strictly positive integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, length, max_value = int(arg_for_seed), int(length), int(max_value)
    if arg_for_seed < 1 or length < 1 or max_value < 1:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed)
L = [randint(1, max_value) for _ in range(length)]
print('Here is L:')
print(L)
print()

size_of_simplest_fraction = None
simplest_fractions = []
size_of_most_complex_fraction = None
most_complex_fractions = []
multiplicity_of_largest_prime_factor = 0
largest_prime_factors = []

from fractions import Fraction
Fra = []
fra= []
for i in L:
    for j in L:
        if Fraction(i,j) < 1:
            fra.append(Fraction(i,j))
        elif Fraction(i,j) == 1:
            fra.append(1/1)
fra = set(fra)
fra = sorted(fra)
for i in fra:
    if not i == 1:
        Fra.append(str(i))
    else:
        Fra.append(str('1/1'))

size_of_simplest_fraction = len(min(Fra,key=len)) - 1
size_of_most_complex_fraction = len(max(Fra,key=len)) - 1

for i in Fra:
    if size_of_most_complex_fraction == size_of_simplest_fraction:
        simplest_fractions.append ( i.split ( '/' ) )
        most_complex_fractions.append ( i.split ( '/' ) )
    else:
        if len(i) == size_of_simplest_fraction + 1:
            simplest_fractions.append(i.split('/'))
        elif len(i) == size_of_most_complex_fraction + 1:
            most_complex_fractions.append(i.split('/'))
most_complex_fractions.reverse ( )

denominators = []
for (x,y) in most_complex_fractions:
    denominators.append(int(y))

def prime(n):
    prime_factors = []
    i = 2
    while i <= n:
        if not n%i == 0:
            i +=1
        else:
            prime_factors.append(i)
            n = n // i
    return prime_factors

list_of_prime = []
list_of_highest = []
for de in denominators:
    list_of_prime = prime(de)
    d = {}
    if list_of_prime :
        for key in list_of_prime:
            d[key] = d.get(key, 0) + 1
        list_of_highest.append(max(d.values()))
    else:
        list_of_highest = [0]
multiplicity_of_largest_prime_factor = max(list_of_highest)

t = []
T = []
for de in denominators:
    list_of_prime = prime ( de )
    d = {}
    if list_of_prime:
        for key in list_of_prime:
            d[ key ] = d.get ( key , 0 ) + 1
        t.append([key for key in d.keys() if d[key]==multiplicity_of_largest_prime_factor])
for i in t:
    for e in i:
        if e:
            T.append(e)
T = set(T)
largest_prime_factors = sorted(T)
print('The size of the simplest fraction <= 1 built from members of L is:',
      size_of_simplest_fraction
     )
print('From smallest to largest, those simplest fractions are:')
print('\n'.join(f'    {x}/{y}' for (x, y) in simplest_fractions))
print('The size of the most complex fraction <= 1 built from members of L is:',
      size_of_most_complex_fraction
     )
print('From largest to smallest, those most complex fractions are:')
print('\n'.join(f'    {x}/{y}' for (x, y) in most_complex_fractions))
print("The highest multiplicity of prime factors of the latter's denominators is:",
      multiplicity_of_largest_prime_factor
     )
print('These prime factors of highest multiplicity are, from smallest to largest:')
print('   ', largest_prime_factors)
        
        
