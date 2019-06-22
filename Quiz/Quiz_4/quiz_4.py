# Randomly fills an array of size 10x10 with True and False, and outputs the number of blocks
# in the largest block construction, determined by rows of True's that can be stacked
# on top of each other. 
#
# Written by Ziheng Sheng and Eric Martin for COMP9021


from random import seed, randrange
import sys


dim = 10


def display_grid():
    for i in range(dim):
        print('     ', end = '')
        print(' '.join(f'{int(e)}' for e in grid[i]))
    print()


def size_of_largest_construction():
    j_recod = []
    max_size = 0
    for i in range(9, -1, -1):
        for j in range(0, 10):
            if (j == 0 and grid[i][j] == 1) or (grid[i][j] == 1 and grid[i][j-1] == 0):
                j_recod.append(j)
        for j_start in j_recod:
            if not j_start == 9:
                j_end = j_start
                while grid[i][j_end] == 1:
                    j_end += 1
                    if j_end == 10:
                        break
                j_end -= 1
            else:
                j_end = j_start
            block_size = int(construction_size(i,j_start,j_end))
            if block_size > max_size:
                max_size = block_size
        #print(j_recod)
        #print(block_size)
        j_recod.clear()
    return max_size


# If j1 <= j2 and the grid has a 1 at the intersection of row i and column j
# for all j in {j1, ..., j2}, then returns the number of blocks in the construction
# built over this line of blocks.
def construction_size(i, j1, j2):
    size = 0
    i_start = i
    while j1 <= j2:
        if grid[i][j1] ==1:
            size += 1
            i -= 1
            if i == -1 or grid[i][j1] != 1:
                j1 += 1
                i = i_start
    return size

            
try:
    for_seed, n = input('Enter two integers, the second one being strictly positive: ').split()
    for_seed = int(for_seed)
    n = int(n)
    if n <= 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(for_seed)
grid = [[bool(randrange(n)) for _ in range(dim)] for _ in range(dim)]
print('Here is the grid that has been generated:')
display_grid()
size = size_of_largest_construction()
if not size:
    print(f'The largest block construction has no block.')  
elif size == 1:
    print(f'The largest block construction has 1 block.')  
else:
    print(f'The largest block construction has {size_of_largest_construction()} blocks.')  
