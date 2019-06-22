# Randomly fills a grid of size 7 x 7 with NE, SE, SW, NW,
# meant to represent North-East, South-East, North-West, South-West,
# respectively, and starting from the cell in the middle of the grid,
# determines, for each of the 4 corners of the grid, the preferred path amongst
# the shortest paths that reach that corner, if any. At a given cell, it is possible to move
# according to any of the 3 directions indicated by the value of the cell;
# e.g., from a cell storing NE, it is possible to move North-East, East, or North.
# At any given point, one prefers to move diagonally, then horizontally,
# and vertically as a last resort.
#
# Written by *** and Eric Martin for COMP9021
import sys
from random import seed, choice
from queue_adt import *

def display_grid():
    for row in grid:
        print('    ', *row)






def preferred_paths_to_corners():
    paths , way , snake= dict ( [ ] ) , dict ( [ ] ) ,Queue ( )
    way['N'] = [-1, 0]
    way['S'] = [1, 0]
    way['W'] = [0, -1]
    way['E'] = [0, 1]
    snake.enqueue ( [ 3 , 3 ] )
    girls = [ [ False for i in range ( dim ) ] for j in range ( dim ) ]
    girls[ 3 ][ 3 ] = True
    bingo = [ [ (i , j) for i in range ( dim ) ] for j in range ( dim ) ]

    while not snake.is_empty ( ):
        r , c = snake.dequeue ( )
        if (r , c) not in corners:
            d1 , d2 = grid[ r ][ c ][ 0 ] , grid[ r ][ c ][ 1 ]
            for t in [ [ r + way[ d1 ][ 0 ] + way[ d2 ][ 0 ] , c + way[ d1 ][ 1 ] + way[ d2 ][ 1 ] ] ,
                       [ r + way[ d1 ][ 0 ] , c + way[ d1 ][ 1 ] ] , [ r + way[ d2 ][ 0 ] , c + way[ d2 ][ 1 ] ] ]:
                if (t[ 0 ] >= 0 and t[ 0 ] < dim) and (t[ 1 ] >= 0 and t[ 1 ] < dim):
                    if not girls[ t[ 0 ] ][ t[ 1 ] ]:
                        girls[ t[ 0 ] ][ t[ 1 ] ] = True
                        snake.enqueue ( t )
                        bingo[ t[ 0 ] ][ t[ 1 ] ] = (r , c)
    for c in corners:
        key = (c[ 1 ] , c[ 0 ])
        if girls[ c[ 0 ] ][ c[ 1 ] ]:
            paths[ key ] = [ c ]
            tmp = c
            while tmp != (size , size):
                paths[ key ] = [ bingo[ tmp[ 0 ] ][ tmp[ 1 ] ] ] + paths[ key ]
                tmp = paths[ key ][ 0 ]
    for k in paths.keys ( ):
        for i in range ( len ( paths[ k ] ) ):
            paths[ k ][ i ] = (paths[ k ][ i ][ 1 ] , paths[ k ][ i ][ 0 ])
    return paths
try:
    seed_arg = int(input('Enter an integer: '))
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
    
seed(seed_arg)
size = 3
dim = 2 * size + 1
grid = [[0] * dim for _ in range(dim)]
directions = 'NE', 'SE', 'SW', 'NW'

grid = [[choice(directions) for _ in range(dim)] for _ in range(dim)]
print('Here is the grid that has been generated:')
display_grid()

corners = (0, 0), (dim - 1, 0), (dim - 1, dim - 1), (0, dim - 1)
paths = preferred_paths_to_corners()
if not paths:
    print('There is no path to any corner')
    sys.exit()
for corner in corners:
    if corner not in paths:
        print(f'There is no path to {corner}')
    else:
        print(f'The preferred path to {corner} is:')
        print('  ', paths[corner])
