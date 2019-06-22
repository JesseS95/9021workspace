
from math import gcd


def fibonacci_decomposition(N, D):
    gcd_ = gcd(N, D)
    N //= gcd_
    D //= gcd_
    if N == 1:
        return [(N, D)]
    d1 = D // N  + 1
    f1_up = N * d1 - D
    f1_down = D * d1
    print((f1_up, f1_down))
    return [(1, d1)] + fibonacci_decomposition(f1_up, f1_down)


L = fibonacci_decomposition(1050, 521)
print(L)


