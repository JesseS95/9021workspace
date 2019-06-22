import os.path
import sys

from collections import defaultdict

print('Please enter the name of the file you want to get data from:',end=' ')
file=input()
if not os.path.exists(file):
    print('Sorry, there is no such file.')
    sys.exit()
origin_data = []
fake_data = []
data=[]
with open(file) as opened_file:
    for rows in opened_file:
        origin_data.append ( rows )
for line in origin_data:
    fake_data.append ( line.strip ( '\n' ).split ( ' ' ) )
for i in fake_data:
    for j in i:
        if j.isdigit():
            data.append(int(j))
        elif not j:
            continue
        else:
            print('Sorry, input file does not store valid data.')
            sys.exit()
for i in data:
    if i <=  0:
        print ( 'Sorry, input file does not store valid data.' )
        sys.exit ( )
if len(data) == 1:
    print ( 'Sorry, input file does not store valid data.' )
    sys.exit ( )
for i in range(len(data)-1):
    if data[i] >= data[i+1]:
        print ( 'Sorry, input file does not store valid data.' )
        sys.exit ( )

longest_length = 0
max_number = 0
panduan = []
panduan_list = []
panduan_list_final = []
length_list = []
def is_dengcha(shulie):
    for i in range(len(shulie)-2):
        if shulie[i+1] - shulie[i] != shulie[i+2] - shulie[i+1]:
            return False
    return True

if is_dengcha(data):
    print ( 'The ride is perfect!' )
    print ( 'The longest good ride has a length of: {}'.format ( len ( data ) -1 ) )
    print ( 'The minimal number of pillars to remove to build a perfect ride from the rest is: 0' )
    sys.exit ( )
else:
    print('The ride could be better...')

    for i in range ( len ( data ) - 2 ):
        if data[ i + 1 ] - data[ i ] == data[ i + 2 ] - data[ i + 1 ]:
            panduan.append ( int ( 1 ) )
        else:
            panduan.append ( int ( 0 ) )
    for i in panduan:
        if i == 0:
            if panduan_list:
                panduan_list_final.append(panduan_list)
                panduan_list = []
            else:
                continue
        if i == 1:
            panduan_list.append ( i )
    for i in panduan_list_final:
        length_list.append(len(i))
    for i in length_list:
        if i >= longest_length:
            longest_length = i
    longest_length += 1

    cat_list = []
    dog_list = []
    sum_dog_list = []
    for i in range(len(data) - 1):
        for j in range(1,len(data)-i):
            cat = data[i+j] - data[i]
            cat_list.append(cat)
        for k in cat_list:
            #print(i,k)
            dog_list = [data[i]]
            dog = data[i] + k
            while dog <= data[-1]:
                if dog in data:
                    dog_list.append(dog)
                    dog += k
                else:
                    break
            #print('dog_list =',dog_list)
            sum_dog_list.append(dog_list)
        cat_list = []
    #print ( sum_dog_list )
    for i in sum_dog_list:
        if max_number <= len(i):
            max_number = len(i)
    min_number = len(data) - max_number
    print ( 'The longest good ride has a length of: {}'.format ( longest_length ) )
    print ( 'The minimal number of pillars to remove to build a perfect ride from the rest is: {}'.format(min_number) )










