# Prompts the user for a strictly positive number N
# and outputs an equilateral triangle of height N.
# The top of the triangle (line 1) is labeled with the letter A.
# For all nonzero p < N, line p+1 of the triangle is labeled
# with letters that go up in alphabetical order modulo 26
# from the beginning of the line to the middle of the line,
# starting wth the letter that comes next in alphabetical order
# modulo 26 to the letter in the middle of line p,
# and then down in alphabetical order modulo 26
# from the middle of the line to the end of the line.


# Insert your code here
import sys
try:
    height = int(input('Enter strictly positive number: '))
    if height <= 0:
        raise ValueError
except ValueError:
    print('Incorrect input, try again.')
    sys.exit()


start = 65
count = 1
row = ''
while count <= (height*(height+1))//2:
    count +=1
    if start > 65 + 25:
        start -= 26
    row += str(chr(start))
    start += 1

row_list = []
start_point = 0
end_point = 1
gap = 1
while end_point <= len(row):
    row_list.append(row[start_point:end_point])
    start_point = end_point
    gap += 1
    end_point += gap

extent_row_list = ['A']
for i in row_list:
    if len(i) >= 2:
        transfer = i
        for j in range(len(i)-2,-1,-1):
            transfer += i[j]
        extent_row_list.append(transfer)

for i in range(height):
    print(' ' * (height - i - 1),end='')
    print(extent_row_list[i])









