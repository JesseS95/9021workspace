import sys
import os


print('Which data file do you want to use?',end=' ')
file=input()
if not os.path.exists(file):
    print('Sorry, there is no such file.')
    sys.exit()
origin_data=[]
fake_data=[]
data=[]
row_data=[]
data_dict = dict()
with open(file) as opened_file:
    for rows in opened_file:
        origin_data.append(rows)
for line in origin_data:
    fake_data.append(line.strip('\n').split(' '))
for i in fake_data:
    for j in i:
        if j.isdigit():
            data.append(int(j))
    row_data.append(list(data))
    data.clear()
for i in range(len(row_data)):
    row_1= row_data[i]
    for i in row_1:
        if i in data_dict:
            data_dict[ i ] += 1
        else:
            data_dict[ i ] = 1
try:
    water = int(input('How many decilitres of water do you want to pour down? '))
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
        if water < 0 :
            raise ValueError
except ValueError:
    print ( 'Incorrect input, giving up.' )
    sys.exit ( )
hight = 0
hight_sort = []
for key in data_dict:
    hight_sort.append(key)
hight_sort.sort()
area_list = []
area = 0
transfer = 0
for i in hight_sort:
    area = (i - (i-1)) * data_dict[i] + area
    area_list.append(int(area)+transfer)
    transfer += int(area)
ha = zip(hight_sort,area_list)
area_dict = dict( (key,value) for key,value in ha)
under_space = 0
sum_under_space = 0
if water <= int(area_dict[hight_sort[0]]):
        hight = hight_sort[0] + water/(data_dict[hight_sort[0]])
elif water > int(area_dict[hight_sort[-1]]):
        for t in range(len(hight_sort)):
            sum_under_space += int(data_dict[hight_sort[t]])
        hight = hight_sort[-1] + (water - int(area_dict[hight_sort[-1]])) / sum_under_space
else:
     for i in range(1,len(hight_sort)):
        if water <= int(area_dict[hight_sort[i]]):
            for t in range(i+1):
                under_space += int(data_dict[hight_sort[t]])
            hight = hight_sort[i] + (water - int(area_dict[hight_sort[i-1]]))/under_space
            break

print('The water rises to {:.2f} centimetres.'.format(hight))










