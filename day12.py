import csv

data = []
with open("day12.txt", 'r') as f:
    r = csv.reader(f)
    for row in r:
        data.append([row[0][:1], int(row[0][1:])])


# Part 1
# turn data into set of commands
# represent position with north, east, and face

# what are our right and left options?
print(set([row[1] for row in data if row[0] in ["R", "L"]]))
# only 90, 180, 270, phew

dirs = ["N", "E", "S", "W"]


class Pos:
    def __init__(self, face, north, east):
        self.face = face  # face must be in dirs
        self.north = north
        self.east = east


def turn(mypos, hand, deg):
    # how far we go (degrees turned into list positions)
    if deg == 90: howmany = 1
    elif deg == 180: howmany = 2
    else: howmany = 3

    # which way we turn (R/L hand turned into positive or negative direction in list)
    if hand == "R":
        whichhand = 1
    else:
        whichhand = -1

    newindex = howmany * whichhand
    oldindex = dirs.index(mypos.face)
    myindex = oldindex + newindex  # if it goes over 3, start counting again from 0. if it goes under 0, start counting again from 3.
    if myindex > 3:
        myindex = myindex - 4
    elif myindex < 0:
        myindex = 4 + myindex

    # pull correct direction from dirs
    mypos.face = dirs[myindex]
    return mypos


def move(mypos, dirs, dist):
    if dirs in ["N", "E"]:
        movement = 1
    else:
        movement = -1
    if dirs in ["E", "W"]:
        mypos.east = mypos.east + dist*movement
    elif dirs in ["N", "S"]:
        mypos.north = mypos.north + dist*movement
    else:
        raise Exception("something went wrong: direction can only be NESW")
    return mypos


mypos = Pos(face="E", north=0, east=0)
for row in data:
    if row[0] in dirs:
        mypos = move(mypos, row[0], row[1])
    elif row[0] == "F":
        mypos = move(mypos, mypos.face, row[1])
    else:
        mypos = turn(mypos, row[0], row[1])
    # print(mypos.face, mypos.north, mypos.east)  # debug
print(abs(mypos.north) + abs(mypos.east))


# Part 2
def follow(mypos, waypos, times):
    mypos = move(mypos, "N", waypos.north*times)
    mypos = move(mypos, "E", waypos.east*times)
    return mypos


def rotate(waypoint, hand, deg):
    n = 0
    e = 0
    if deg == 180:  # 180 means change the signs
        n = waypoint.north * -1
        e = waypoint.east * -1
    elif deg == 90:
        if hand == "R":
            n = waypoint.east * -1
            e = waypoint.north
        else:
            n = waypoint.east
            e = waypoint.north * -1
    elif deg == 270:
        if hand == "R":
            n = waypoint.east
            e = waypoint.north * -1
        else:
            n = waypoint.east * -1
            e = waypoint.north
    return Pos(face="N", north=n, east=e)


waypoint = Pos(face="N", north=1, east=10)
ship = Pos(face="E", north=0, east=0)
for row in data:
    if row[0] in dirs:
        waypoint = move(waypoint, row[0], row[1])
    elif row[0] == "F":
        ship = follow(ship, waypoint, row[1])
    else:
        waypoint = rotate(waypoint, row[0], row[1])
print(abs(ship.north) + abs(ship.east))
