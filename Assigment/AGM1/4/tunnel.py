import os.path
import sys
from collections import deque
print('Please enter the name of the file you want to get data from:',end=' ')
file=input()
if not os.path.exists(file):
    print('Sorry, there is no such file.')
    sys.exit()
origin_data = []
fake_data = []
data = []
data1 = []
data2 = []
with open(file) as opened_file:
    for rows in opened_file:
        origin_data.append(rows)
for line in origin_data:
    fake_data.append(line.strip('\n').split(' '))
for i in fake_data:
    if i == ['']:
        continue
    else:
        data.append(i)
if len(data) != 2:
    print('Sorry, input file does not store valid data.')
    sys.exit()
for i in data[0]:
    if i.isdigit ( ):
        data1.append ( int ( i ) )
    elif not i:
        continue
    else:
        print ( 'Sorry, input file does not store valid data.' )
        sys.exit ( )
for i in data[1]:
    if i.isdigit ( ):
        data2.append ( int ( i ) )
    elif not i:
        continue
    else:
        print ( 'Sorry, input file does not store valid data.' )
        sys.exit ( )
if len(data1) != len(data2):
    print ( 'Sorry, input file does not store valid data.' )
    sys.exit ( )
if len(data1) <= 1:
    print ( 'Sorry, input file does not store valid data.' )
    sys.exit ( )
for i in range(len(data1)):
    if data1[i] <= data2[i]:
        print ( 'Sorry, input file does not store valid data.' )
        sys.exit ( )

data1_set = data1[0]
data2_set = data2[0]
yanguang1 = 1
for i in range(1,len(data1)):
    if (data1[i] >= data1_set) & (data2[i] <= data2_set):
        yanguang1 += 1
    elif (data1[i] < data1_set) & (data2[i] > data2_set):
        data1_set = data1[i]
        data2_set = data2[i]
        yanguang1 += 1
    else:
        if (data1[i] >= data1_set) & (data2[i] > data2_set):
            if data2[i] >= data1_set:
                break
            else:
                data2_set = data2[i]
                yanguang1 += 1
        elif (data1[i] < data1_set) & (data2[i] <= data2_set):
            if data1[i] <= data2_set:
                break
            else:
                data1_set = data1[i]
                yanguang1 += 1

yanguang2_list = []
max_yanguang2 = 0
for j in range(len(data1)):
    yanguang2 = 1
    data1_set1 = data1[j]
    data2_set1 = data2[j]
    for i in range ( j+1 , len ( data1 ) ):
        if (data1[ i ] >= data1_set1) & (data2[ i ] <= data2_set1):
            yanguang2 += 1
        elif (data1[ i ] < data1_set1) & (data2[ i ] > data2_set1):
            data1_set1 = data1[ i ]
            data2_set1 = data2[ i ]
            yanguang2 += 1
        else:
            if (data1[ i ] >= data1_set1) & (data2[ i ] > data2_set1):
                if data2[ i ] >= data1_set1:
                    break
                else:
                    data2_set1 = data2[ i ]
                    yanguang2 += 1
            elif (data1[ i ] < data1_set1) & (data2[ i ] <= data2_set1):
                if data1[ i ] <= data2_set1:
                    break
                else:
                    data1_set1 = data1[ i ]
                    yanguang2 += 1
    yanguang2_list.append(yanguang2)
for i in yanguang2_list:
    if max_yanguang2 <= i:
        max_yanguang2 = i

print('From the west, one can see into the tunnel over a distance of {}.'.format(yanguang1))
print('Inside the tunnel, one can see into the tunnel over a maximum distance of {}.'.format(max_yanguang2))

