# Uses Global Temperature Time Series, avalaible at
# http://data.okfn.org/data/core/global-temp, stored in the file monthly_csv.csv,
# assumed to be stored in the working directory.
# Prompts the user for the source, a year or a range of years, and a month.
# - The source is either GCAG or GISTEMP.
# - The range of years is of the form xxxx -- xxxx (with any number of spaces,
#   possibly none, around --) and both years can be the same,
#   or the first year can be anterior to the second year,
#   or the first year can be posterior to the first year.
# We assume that the input is correct and the data for the requested month
# exist for all years in the requested range.
# Then outputs:
# - The average of the values for that source, for this month, for those years.
# - The list of years (in increasing order) for which the value is larger than that average.
# 
# Written by Ziheng Sheng and Eric Martin for COMP9021
import sys
import os
import csv
filename = 'monthly_csv.csv'
if not os.path.exists(filename):
    print(f'There is no file named {filename} in the working directory, giving up...')
    sys.exit()

source = input('Enter the source (GCAG or GISTEMP): ')
year_or_range_of_years = input('Enter a year or a range of years in the form XXXX -- XXXX: ')
month = input('Enter a month: ')
average = 0
years_above_average = []
a_year = int(year_or_range_of_years[:4])
b_year = int(year_or_range_of_years[-4:])
min_year = min(a_year,b_year)
max_year = max(a_year,b_year)
target_row = []
d_month = {
    'January':'01',
    'February':'02',
    'March':'03',
    'April':'04',
    'May':'05',
    'June':'06',
    'July':'07',
    'August':'08',
    'September':'09',
    'October':'10',
    'November':'11',
    'December':'12'
}
month_number = d_month[month]
with open (filename) as f:
    t = csv.reader(f)
    for row in t:
        if row[0] == source:
            if int(min_year) <= int(row[1][:4]) <= int(max_year):
                if row[1][5:7] == month_number:
                    target_row.append(row)
sum_target_data = 0
for i in target_row:
    sum_target_data += float(i[2])
average = sum_target_data/len(target_row)
for i in target_row:
    if float(i[2]) > average:
        years_above_average.append(int(i[1][:4]))
years_above_average.sort()
print(f'The average anomaly for {month} in this range of years is: {average:.2f}.')
print('The list of years when the temperature anomaly was above average is:')
print(years_above_average)
