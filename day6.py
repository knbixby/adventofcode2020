import csv

data = []
with open("day6.txt", 'r') as f:
    r = csv.reader(f)
    for row in r:
        data.append(row)

# Part 1
# added extra newline to end of data so this works
plane = {}
group = 0
person = 0
dec = {}
for row in data:
    if not row:
        group += 1
        plane[group] = dec
        dec = {}
        person = 0
    else:
        dec[person] = row[0]
        person += 1

# sum of set of letter responses within group
total = 0
for group in plane:
    count = len(set("".join([plane[group][i] for i in plane[group]])))
    total += count
print(total)


# Part 2
# sum of set of letter responses common to every person in a group
total = 0
for group in plane:
    responses = [set(plane[group][i]) for i in plane[group]]
    myset = responses[0]
    for each in responses:
        myset = myset.intersection(each)
    total += len(myset)
print(total)
