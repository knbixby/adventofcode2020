import re
import csv
import copy


data = []
with open("day24.txt", 'r') as f:
    r = csv.reader(f)
    for row in r:
        data.append(row)

# Part 1
translate = {
    "nw": (-1, 1),
    "ne": (0, 1),
    "w": (-1, 0),
    "e": (1, 0),
    "sw": (0, -1),
    "se": (1, -1)
}
# nw ne
#  w . e
#   sw se

dirs = []

for row in data:
    newrow = []
    for m in re.findall(r"(ne|nw|se|sw|e|w)", row[0]):
        newrow.append(translate[m])
    dirs.append(newrow)

# then keep track of which tiles are flipped. face: white, back: black
flips = {}
for row in dirs:
    x, y = sum([i[0] for i in row]), sum([i[1] for i in row])
    if (x, y) in flips:
        flips[(x, y)] = flips[(x, y)] + 1
    else:
        flips[(x, y)] = 1

x = 0
for each in flips:
    if flips[each] % 2 != 0:
        flips[each] = True
        x += 1
    else:
        flips[each] = False
print(x)


# Part 2
def neighbors(a):
    # we can move to a neighbor by moving in each of our translate directions
    return([(a[0]+translate[i][0], a[1]+translate[i][1]) for i in translate])

# Any black tile with zero or more than 2 black tiles immediately adjacent to it is flipped to white.
# Any white tile with exactly 2 black tiles immediately adjacent to it is flipped to black.

for x in range(100):
    f = copy.deepcopy(flips)
    for each in flips.keys():
        for i in neighbors(each):
            if i not in flips:
                flips[i] = False
    for each in flips:
        c = sum([flips[i] if i in flips else False for i in neighbors(each)])
        if flips[each] and (c == 0 or c > 2):
            f[each] = False
        elif not flips[each] and c == 2:
            f[each] = True
    flips = f

print(sum(flips.values()))
