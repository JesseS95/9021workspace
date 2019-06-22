import csv
from collections import defaultdict


_dict = defaultdict(list)
tmp_list = []
indicator = input("Enter an Indicator Name: ")

file_name = 'HNP_Data.csv'
with open(file_name) as file:
    csv_file = csv.reader(file)
    max_number = 0
    for rows in csv_file:
        if rows[2] == indicator:
            for i in range(5, len(rows)):
                if rows[i] != '':
                    if float(rows[i]) >= max_number:
                        tmp_list.append((i + 1956, rows[0], float(rows[i])))
                        # _dict[i + 1956].append(rows[0])
                        max_number = float(rows[i])
print(max_number)
print(tmp_list)

for _tuples in tmp_list:
    if _tuples[2] == max_number:
        _dict[_tuples[0]].append(_tuples[1])
print(_dict)