import sys
from math import factorial


def first_computation(x):
	t = 0
	while x%10 == 0:
		t += 1
		x //= 10
	return t

def second_computation(x):
	k = 0
	p = str(x)
	for i in range(len(p)-1,-1,-1):
		if p[i] == '0':
			k += 1
		else:
			break
	return k

def third_computation(x):
	k = 0
	t = 5
	while x >= t:
		k += x // t
		t *= 5
	return k
try:
	the_input = int(input('Input a nonnegative integer: '))
	if the_input < 0:
		raise ValueError
except ValueError:
	print('Incorrect input, giving up.')
	sys.exit()

the_input_factorial = factorial(the_input)
print(f'Computing the number of trailing 0s in {the_input}! by dividing by 10 for long enough:',
      first_computation(the_input_factorial))
print(f'Computing the number of trailing 0s in {the_input}! by converting it into a string:',
      second_computation(str(the_input_factorial)))
print(f'Computing the number of trailing 0s in {the_input}! the smart way:',
      third_computation(the_input))
