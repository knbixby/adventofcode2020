import csv

data = []
with open("day5.txt", 'r') as f:
    r = csv.reader(f)
    for row in r:
        data.append(row)

# Part 1
# 128 rows on plane labeled 0-127
# 8 columns on plane labeled 0-7
# f lower, b higher; l is lower, r is higher

# each seat id is row * 8 plus the column
# find the highest possible seat id

seats = []
for row in data:
    rowcode = row[0][:7]
    colcode = row[0][7:]

    rows = (0, 128)
    for each in rowcode:
        if each == "F":
            rows = (rows[0], ((rows[1]-rows[0])/2 + rows[0]))
        elif each == "B":
            rows = (((rows[1]-rows[0])/2 + rows[0]), rows[1])
    rownum = rows[0]

    cols = (0, 8)
    for each in colcode:
        if each == "L":
            cols = (cols[0], ((cols[1]-cols[0])/2 + cols[0]))
        elif each == "R":
            cols = (((cols[1]-cols[0])/2 + cols[0]), cols[1])
    colnum = cols[0]

    seat = (rownum * 8) + colnum

    seats.append(seat)

print(max(seats))

# Part 2
for num in range(min(seats), max(seats)):
    if num not in seats:
        print(num)
