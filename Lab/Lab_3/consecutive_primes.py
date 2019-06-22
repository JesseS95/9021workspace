from math import sqrt

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2,round(sqrt(n) +1)):
        if n % i == 0:
            return False
    return True
print('The solutions are: ',end='\n\n')
for i in range(10000, 99969):
    if not is_prime(i):
        continue
    b = i + 2
    if not is_prime(b):
        continue
    c = b + 4
    if not is_prime(c):
        continue
    d = c + 6
    if not is_prime(d):
        continue
    e = d + 8
    if not is_prime(e):
        continue
    f = e + 10
    if not is_prime(f):
        continue
    count = 0
    for j in range(i,f+1):
        if is_prime(j):
            count += 1
    if count == 6:
        print(i,b,c,d,e,f)