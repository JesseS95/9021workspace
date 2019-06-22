

def validate_9_puzzle(grid):
    if len(grid) != 3:
        print("This is an invalid or unsolvable 9 puzzle")
        return
    long_list = []
    counter = 0
    for i in range(len(grid)):
        if len(grid[i]) != 3:
            print("This is an invalid or unsolvable 9 puzzle")
            return
        for j in range(len(grid[i])):
            if grid[i][j]:
                long_list.append(grid[i][j])
    if len(set(long_list)) != 8:
        print("This is an invalid or unsolvable 9 puzzle")
        return
    for i in range(len(long_list)):
        for j in range(i+1, len(long_list)):
            if long_list[j] < long_list[i]:
                counter += 1
    print(counter)
    if counter % 2 == 0:
        print("This is a valid 9 puzzle, and it is solvable")
    else:
        print("This is an invalid or unsolvable 9 puzzle")



