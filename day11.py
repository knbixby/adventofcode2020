import csv
import copy

data = []
with open("day11.txt", 'r') as f:
    r = csv.reader(f)
    for row in r:
        data.append(list(row[0]))

# adjacent seats are directly next to it left, right, up, down, and all diagonals
# L is a seat, . is floor
# If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
# If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
# how many occupied seats when stabilizes?


def find_adjacent(i, j):
    # i row, j col
    seats = []
    for num1 in range(i-1, i+2):
        for num2 in range(j-1, j+2):
            seats.append((num1, num2))
    seats.remove((i, j))
    badseats = [seat for seat in seats if ((seat[0] >= len(data) or seat[0] < 0) or (seat[1] >= len(data[0]) or seat[1] < 0))]
    for seat in badseats:
        seats.remove(seat)
    return seats

room = copy.deepcopy(data)

# within while loop
change = True
while change:
    newRoom = copy.deepcopy(room)
    print("reset room")
    for i, row in enumerate(room):
        for j, col in enumerate(row):
            adjSeatLocs = find_adjacent(i, j)
            adjSeats = [room[loc[0]][loc[1]] for loc in adjSeatLocs]
            if newRoom[i][j] == ".":
                pass
            elif adjSeats.count("#") == 0:
                newRoom[i][j] = "#"
            elif adjSeats.count("#") > 3:
                newRoom[i][j] = "L"
            else:
                continue
    if room == newRoom:
        change = False
        print(sum([1 for row in room for col in row if col == "#"]))
        break
    room = newRoom


# Part 2
def find_adjacent_nofloor(i, j):
    # could speed this up a lot by doing this step only once and storing results for each coordinates in dict
    # since the floor doesn't change
    # i row, j col, use data
    seats = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    length = range(len(data))
    width = range(len(data[0]))
    for d in directions:
        notFound = True
        num1 = i
        num2 = j
        while notFound:
            num1+=d[0]
            num2+=d[1]
            if num1 in length and num2 in width:
                if data[num1][num2] == ".":
                    continue
                else:
                    seats.append((num1, num2))
                    notFound = False
            else:
                notFound = False
                break
    return seats


room = copy.deepcopy(data)

# within while loop
change = True
c = 0
while change:
    newRoom = copy.deepcopy(room)
    print("reset room %s" % c)
    c += 1
    for i, row in enumerate(room):
        for j, col in enumerate(row):
            adjSeatLocs = find_adjacent_nofloor(i, j)
            adjSeats = [room[loc[0]][loc[1]] for loc in adjSeatLocs]
            if newRoom[i][j] == ".":
                pass
            elif adjSeats.count("#") == 0:
                newRoom[i][j] = "#"
            elif adjSeats.count("#") > 4:
                newRoom[i][j] = "L"
            else:
                continue
    # for row in newRoom:
    #     print("".join(row))
    if room == newRoom:
        change = False
        print(sum([1 for row in room for col in row if col == "#"]))
        break
    room = newRoom



