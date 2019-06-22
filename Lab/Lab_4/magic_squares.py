
def is_magic(square):
    _sum = sum(square[0])
    sum_of_ax1 = 0
    sum_of_ax2 = 0
   # print(_sum)
    for i in range(len(square)):
        sum_of_column = 0
        sum_of_ax1 += square[i][i]
        sum_of_ax2 += square[i][len(square) - 1 - i]
        if sum(square[i]) != _sum:
            return False
        for j in range(len(square)):
            sum_of_column += square[j][i]
        #print(sum_of_column)
        if sum_of_column != _sum:
            return False
    #print(sum_of_ax1, sum_of_ax2)
    if sum_of_ax1 != _sum or sum_of_ax2 != _sum:
        return False
    return True





square = [[2,7,6], [1,5,9], [4,3,8]]
print(is_magic(square))