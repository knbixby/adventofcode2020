import csv

data = []
with open("day10.txt", 'r') as f:
    r = csv.reader(f)
    for row in r:
        data.append(int(row[0]))


# Part 1
data.sort()
data = [0] + data + [data[-1]+3]  # must add the wall (starts at 0) and the device (3 above last adapter)
diffs = [data[i+1]-data[i] for i in range(len(data)-1)]
print(diffs.count(1) * diffs.count(3))


# Part 2
# how many unique arrangements are there

# Attempt 1
p = []
for num in data[:-1]:
    c = 0
    for n in range(1, 4):
        if num + n in data:
            c += 1
    p.append(c)

prod = 1
for each in p:
    prod = prod * each
print(prod)  # 5 orders of magnitude too large
# this made too many because some possibilities aren't real; can only have 1-3 difference between each


# Attempt 2
# go backwards
p = {0: 1}  # store all actual possibilities
for num in data[1:]:
    c = []  # count cumulative possibilities
    for n in range(1, 4):
        if num - n in p:
            c.append(p[num-n])
    p[num] = sum(c)

device = data[-1]
print(p[device])
