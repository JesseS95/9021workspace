from math import sqrt


def could_decom(n):
    for i in range(round(sqrt(n) + 1)):
        for j in range(i, round(sqrt(n) + 1)):
            if i ** 2 + j ** 2 == n:
                return (i, j)
    return False

_list = []
for i in range(100, 997):
    if could_decom(i) and could_decom(i+1) and could_decom(i+2):
        print ( '({}, {}, {}) (equal to ({}^2+{}^2, {}^2+{}^2, {}^2+{}^2)) is a solution.'.format(i,i+1,i+2,could_decom(i)[0],could_decom(i)[1],could_decom(i+1)[0],could_decom(i+1)[1],could_decom(i+2)[0],could_decom(i+2)[1]))
i