import csv

data = []
with open("day3.txt", 'r') as f:
    r = csv.reader(f)
    for row in r:
        data.append(row)

# Part 1
trees = 0
repeat = len(data[0][0])
pos = 0
for row in data:
    if row[0][pos] == "#":
        trees += 1
    pos += 3
    if pos >= repeat:
        pos = 0 + (pos-repeat)
print(trees)

# Part 2
# collect number of trees hit for the following paths
# 1d, 1r
# 1d, 3r
# 1d, 5r
# 1d, 7r
# 2d, 1r
trees = []
for down, distance in [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]:
    tree = 0
    repeat = len(data[0][0])
    pos = 0
    for i in range(len(data)):
        if i % down == 0:
            if data[i][0][pos] == "#":
                tree += 1
            pos += distance
            if pos >= repeat:
                pos = 0 + (pos-repeat)
    trees.append(tree)
print(trees)

print(78*247*68*69*33)




