# Randomly fills an array of size 10x10 True and False, displayed as 1 and 0,
# and outputs the number chess knights needed to jump from 1s to 1s
# and visit all 1s (they can jump back to locations previously visited).
#
# Written by zhsheng and Eric Martin for COMP9021


from random import seed, randrange
import sys


dim = 10
position_8 = [ (2 , -1) , (2 , 1) , (1 , 2) , (-1 , 2) , (-2 , 1) , (-2 , -1) , (-1 , -2) , (1 , -2) ]

def display_grid():
    for i in range(dim):
        print('     ', end = '')
        print(' '.join(grid[i][j] and '1' or '0' for j in range(dim)))
    print()

def explore_board():
    count = 0
    for i in range(dim):
        for j in range(dim):
            if grid[i][j]:
                count += 1
                if position_check(i,j):
                    continue
            else:
                continue
    return count

def position_check(i,j):
    for _ in position_8:
        xiayibu = (i + _[ 0 ] , j + _[ 1 ])
        if 0 <= xiayibu[ 0 ] < 10 and 0 <= xiayibu[ 1 ] < 10 :
            if grid[ xiayibu[ 0 ] ][ xiayibu[ 1 ] ] == 1:
                grid[ xiayibu[ 0 ] ][ xiayibu[ 1 ] ] = 0
                position_check(xiayibu[ 0 ],xiayibu[ 1 ])
            else:
                continue
        else:
            continue
    return True

try:
    for_seed, n = (int(i) for i in input('Enter two integers: ').split())
    if not n:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(for_seed)
if n > 0:
    grid = [[randrange(n) > 0 for _ in range(dim)] for _ in range(dim)]
else:
    grid = [[randrange(-n) == 0 for _ in range(dim)] for _ in range(dim)]    
print('Here is the grid that has been generated:')
display_grid()
nb_of_knights = explore_board()
if not nb_of_knights:
    print('No chess knight has explored this board.')
elif nb_of_knights == 1:
    print(f'At least 1 chess knight has explored this board.')
else:
    print(f'At least {nb_of_knights} chess knights have explored this board')

