import re
import csv
import collections


data = []
with open("day14.txt", 'r') as f:
    r = csv.reader(f)
    for row in r:
        data.append(row)


# Part 1
# create dictionary of masks with their memory locations and numbers to convert
d = collections.OrderedDict()  # it took me way too long to realize order matters (because overwriting)
for row in data:
    if row[0].startswith("mask"):
        m = row[0][-36:]
        d[m] = collections.OrderedDict()
    elif row[0].startswith("mem"):
        d[m][int(re.search("(?<=\[)\d+(?=\])", row[0]).group())] = int(re.search("(?<=\=\s)\d+$", row[0]).group())
    else:
        print(row)


def cronch(num):
    newnum = str(bin(num)).lstrip("0b")
    while len(newnum) < 36:
        newnum = "0" + newnum
    return newnum


def uncronch(num):
    return int(num, 2)


def mask(m, num):
    num = list(num)
    for i, c in enumerate(m):
        if c != "X":
            num[i] = c
    num = "".join(num)
    return num


mem = {}  # my "computer's" memory
for m in d:
    for loc in d[m]:
        mem[loc] = uncronch(mask(m, cronch(d[m][loc])))

print(sum(mem.values()))


# Part 2
def cronch2(num, length):
    newnum = str(bin(num)).lstrip("0b")
    while len(newnum) < length:
        newnum = "0" + newnum
    return newnum


def mask2(m, num):
    nums = []
    num = list(num)
    for i, c in enumerate(m):
        if c != "0":
            num[i] = c
    x = [i for i, c in enumerate(num) if c == "X"]
    for each in range(2 ** len(x)):
        xes = cronch2(each, len(x))
        for j in range(len(xes)):
            ch = list(xes)
            num[x[j]] = ch[j]
        newnum = "".join(num)
        nums.append(newnum)
    return nums


mem = {}  # my "computer's" memory
for m in d:
    for loc in d[m]:
        for each in mask2(m, cronch(loc)):
            mem[uncronch(each)] = d[m][loc]
print(sum(mem.values()))
