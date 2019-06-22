from collections import defaultdict


def if_valid(grid):
    if len(grid) != 3:
        return False
    all_number = []
    for i in range(len(grid)):
        if len(grid[i]) != 3:
            return False
        for j in range(len(grid)):
            if grid[i][j]:
                all_number.append(grid[i][j])
    _all_number = sorted(all_number)
    if len(_all_number) != 8:
        return False
    for i in range(len(_all_number)):
        if _all_number[i] != i+1:
            return False
    
    count_of_inversion = 0
    # info = defalutdict(int)
    for i in range(len(all_number) - 1):
        for j in range(i + 1, len(all_number)):
            if all_number[j] < all_number[i]:
                count_of_inversion += 1
    
    if count_of_inversion % 2 == 0:
        return True
    else:
        return False


print(if_valid([[4, None, 8], [1, 3, 7], [5, 2, 6]]))