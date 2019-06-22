def nb_of_consecutive_squares(n):
    if not sums_of_two_squares[n]:
        return 0
    if not sums_of_two_squares[n + 1]:
        return 1
    if not sums_of_two_squares[n + 2]:
        return 2
    return 3


sums_of_two_squares = [None] * 1_000
for i in range(32):
    for j in range(i, 32):
        n = i * i + j * j
        if n < 100:
            continue
        if n >= 1_000:
            break
        sums_of_two_squares[n] = i, j
for n in range(100, 1_000):
    i = nb_of_consecutive_squares(n)
    if i < 3:
        n += i
        continue
    print(f'({n}, {n + 1}, {n + 2}) (equal to ('
                                    f'{sums_of_two_squares[n][0]}^2+{sums_of_two_squares[n][1]}^2, '
                            f'{sums_of_two_squares[n + 1][0]}^2+{sums_of_two_squares[n + 1][1]}^2, '
                              f'{sums_of_two_squares[n + 2][0]}^2+{sums_of_two_squares[n + 2][1]}^2'
                                                                                 ')) is a solution.'
         )
    # We assume we could have two solutions of the form
    # (n, n + 1, n + 2) and (n + 1, n + 2, n + 3)
    # (but as the solution shows, this never happens...),
    # hence n is incremented by only 1 in the next iteration of the loop.
    # We could avoid checking that sums_of_two_squares[n + 1] and
    # sums_of_two_squares[n + 2] are not equal to 0, but why make the program
    # more complicated for no significant gain?

