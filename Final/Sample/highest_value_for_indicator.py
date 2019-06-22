import csv
from collections import defaultdict



Indicator = input("Enter an Indicator Name: ")
dic = defaultdict(list)


with open('HNP_Data.csv') as f:
    csv_file = csv.reader(f)
    for rows in csv_file:
        if rows[2] == Indicator:
            for i in range(len(rows[4: ])):
                if rows[4: ][i]:
                    dic[(rows[4: ][i], i + 1960)].append(rows[0])

max_value = max(dic, key = lambda x: float(x[0]))[0]
print(max_value)

for _tuple in dic:
    if _tuple[0] == max_value:
        print(f'{_tuple[1]}, {dic[_tuple]}')