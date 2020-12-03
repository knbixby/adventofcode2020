import re
import csv

data = []
with open("day2.txt", 'rU') as f:
    r = csv.reader(f)
    for row in r:
        data.append(row)

# Part 1
# parse each line into data
pdata = []
for row in data:
    i = re.search(":", row[0]).start()
    j = re.search("-", row[0]).start()
    pdata.append([int(row[0][0:j]), int(row[0][j+1:i-2]), row[0][i-1], row[0][i+2:]])

count = 0
for row in pdata:
    if row[0] <= len(re.findall(row[2], row[3])) <= row[1]:
        count += 1

print(count)

# Part 2
# now only one of the (1-indexed) locations must contain the specified character
# it's XOR
count = 0
for row in pdata:
    i1 = row[0]-1  # get the corrected indices
    i2 = row[1]-1
    if row[3][i1] == row[2] and row[3][i2] == row[2]:
        pass
    elif row[3][i1] == row[2] or row[3][i2] == row[2]:
        count += 1

print(count)
