import csv
import copy

origdata = []
with open("day17.txt", 'r') as f:
    r = csv.reader(f)
    for row in r:
        origdata.append(list(row[0]))


# Part 1

# 6 cycles
# each cube only looks at the 26 other cubes directly adjacent
# if it's active, and 2 or 3 cubes around it are active, no change
# if active, but different number, changes to inactive
# if inactive, and 3 cubes only around it are active, it becomes active
# if inactive and any other number, no change

# create the set i need to consider: only 6 cycles
a = 13
b = 20
c = 20
data = [[["."] * c for _ in range(b)] for _ in range(a)]
for i, row in enumerate(origdata):
    data[6][i+5][5:13] = row[:]

# now go through the whole thing with those rules

def getcoords(i, j, k):
    coordlist = []
    for n in range(i-1, i+2):
        for m in range(j-1, j+2):
            for o in range(k-1, k+2):
                coordlist.append((n, m, o))
    badcoord = []
    for each in coordlist:
        if each[0] < 0 or each[1] < 0 or each[2] < 0:
            badcoord.append(each)
        elif each[0] > a-1:
            badcoord.append(each)
        elif each[1] > b-1 or each[2] > c-1:
            badcoord.append(each)
    for each in badcoord:
        coordlist.remove(each)
    coordlist.remove((i, j, k))
    return coordlist

c3 = {}
for i in range(a):
    for j in range(b):
        for k in range(c):
            c3[(i, j, k)] = getcoords(i, j, k)

for cycle in range(6):
    newcube = copy.deepcopy(data)
    for i in range(a):
        for j in range(b):
            for k in range(c):
                # get all my things
                cu = [data[t[0]][t[1]][t[2]] for t in c3[(i, j, k)]]
                # apply the rules
                if data[i][j][k] == "#":
                    if 1 < cu.count("#") < 4:
                        pass
                    else:
                        newcube[i][j][k] = "."
                else:
                    if cu.count("#") == 3:
                        newcube[i][j][k] = "#"
    data = newcube

count = 0
for i in range(a):
    for j in range(b):
        for k in range(c):
            if data[i][j][k] == "#":
                count += 1
print(count)


# Part 2

# just put it all in 4 dimensions
z = 13
a = 13
b = 20
c = 20
data = [[[["."] * c for _ in range(b)] for _ in range(a)] for _ in range(z)]
for i, row in enumerate(origdata):
    data[6][6][i+5][5:13] = row[:]

# now go through the whole thing with those rules

def getcoords(h, i, j, k):
    coordlist = []
    for p in range(h-1, h+2):
        for n in range(i-1, i+2):
            for m in range(j-1, j+2):
                for o in range(k-1, k+2):
                    coordlist.append((p, n, m, o))
    badcoord = []
    for each in coordlist:
        if each[0] < 0 or each[1] < 0 or each[2] < 0 or each[3] < 0:
            badcoord.append(each)
        elif each[0] > a-1 or each[1] > z-1:
            badcoord.append(each)
        elif each[2] > b-1 or each[3] > c-1:
            badcoord.append(each)
    for each in badcoord:
        coordlist.remove(each)
    coordlist.remove((h, i, j, k))
    return coordlist

c3 = {}
for h in range(z):
    for i in range(a):
        for j in range(b):
            for k in range(c):
                c3[(h, i, j, k)] = getcoords(h, i, j, k)

for cycle in range(6):
    newcube = copy.deepcopy(data)
    for h in range(z):
        for i in range(a):
            for j in range(b):
                for k in range(c):
                    # get all my things
                    cu = [data[t[0]][t[1]][t[2]][t[3]] for t in c3[(h, i, j, k)]]
                    # apply the rules
                    if data[h][i][j][k] == "#":
                        if 1 < cu.count("#") < 4:
                            pass
                        else:
                            newcube[h][i][j][k] = "."
                    else:
                        if cu.count("#") == 3:
                            newcube[h][i][j][k] = "#"
    data = newcube

count = 0
for h in range(z):
    for i in range(a):
        for j in range(b):
            for k in range(c):
                if data[h][i][j][k] == "#":
                    count += 1
print(count)
