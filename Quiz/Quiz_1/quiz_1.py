# Written by ZH Sheng and Eric Martin for COMP9021
import sys
from random import seed, randrange

try:
    arg_for_seed = int(input('Enter an integer: '))
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed)
x = randrange(10 ** 10)
sum_of_digits_in_x = 0
L = [randrange(10 ** 8) for _ in range(10)]
first_digit_greater_than_last = 0
same_first_and_last_digits = 0
last_digit_greater_than_first = 0
distinct_digits = [0] * 9
min_gap = 10
max_gap = -1
first_and_last = set()

gap=[]
l_of_fl=[]
str_x=str(x)
for i in range(len(str_x)):
    sum_of_digits_in_x+=int(str_x[i])
for i in L:
    str_l=str(i)
    if str_l[0]>str_l[-1]:
        first_digit_greater_than_last+=1
        gap.append(int(str_l[0])-int(str_l[-1]))
    elif str_l[0]==str_l[-1]:
        same_first_and_last_digits+=1
        gap.append ( 0 )
    else:
        last_digit_greater_than_first+=1
        gap.append ( int ( str_l[ -1 ] ) - int ( str_l[ 0 ] ) )
    str_l_set = set(str_l)
    distinct_digits[len(str_l_set)]+=1
    fl=int(str_l[0]),int(str_l[-1])
    l_of_fl.append(fl)

d=dict()
for i in l_of_fl:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
max_value_L = max(d.values())
first_and_last=[ key for key in d.keys() if d[key]==max_value_L ]
max_gap=max(gap)
min_gap=min(gap)

print()
print('x is:', x)
print('L is:', L)
print()
print(f'The sum of all digits in x is equal to {sum_of_digits_in_x}.')
print()
print(f'There are {first_digit_greater_than_last}, {same_first_and_last_digits} '
      f'and {last_digit_greater_than_first} elements in L with a first digit that is\n'
      '  greater than the last digit, equal to the last digit,\n'
      '  and smaller than the last digit, respectively.'
     )
print()
for i in range(1, 9):
    if distinct_digits[i]:
        print(f'The number of members of L with {i} distinct digits is {distinct_digits[i]}.')
print()
print('The minimal gap (in absolute value) between first and last digits\n'
      f'  of a member of L is {min_gap}.'
     )
print('The maximal gap (in absolute value) between first and last digits\n'
      f'  of a member of L is {max_gap}.')
print()
print('The number of pairs (f, l) such that f and l are the first and last digits\n'
      f'of members of L is maximal for (f, l) one of {sorted(first_and_last)}.'
     )
        
