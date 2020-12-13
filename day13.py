import csv

data = []
with open("day13.txt", 'r') as f:
    r = csv.reader(f)
    for row in r:
        data.append(row)

# Part 1
# bus name is bus time
# get earliest bus after mytime

mytime = int(data[0][0])
buses = data[1]

b = {}  # store buses and my wait times
for each in buses:
    if each != "x":
        n = int(each)
        b[n - (mytime % n)] = n  # store key of the diff between my time mod the bus time, with bus name as the value
lowest = min(b.keys())  # this is my best bus, or lowest wait time
print(lowest * b[lowest])  # multiply bus name by how long it is after mytime


# Part 2
# at what timestamp will the buses depart at consecutive timestamps matching their index in the list?
times = [i for i, bus in enumerate(buses) if bus != "x"]
bus = [int(bus) for bus in buses if bus != "x"]
# timestamp for which the (timestamp + times) % bus# for all buses is 0


# # Attempt 1: takes forever
# # faster to increment by only the multiples of the largest bus, 431
# x = max(bus)
# ind = bus.index(x)
# time = x - times[ind]  # start our time at the correct number (t0 is the largest minus its time offset)
#
# found = False
# while not found:
#     t = [i + time for i in times]  # here's all the correct offsets given the start time
#     if sum([t[i] % bus[i] for i in range(len(bus))]) == 0:  # offset time mod bus number for all buses is 0
#         print(time)
#         found = True
#     time += x


# # Attempt 2
# # attempt 1 worked for the example but it's taking too long. solve for the two largest numbers and increment by that.
# # get the two largest bus numbers and their offset times
# x1 = max(bus)
# ind1 = bus.index(x1)
# x2 = max([each for each in bus if each != x1])
# ind2 = bus.index(x2)
# # start at the largest time like in Attempt 1
# time = x1 - times[ind1]
# # make the smaller example with two largest buses
# tinybus = [x1, x2]
# tinytimes = [times[ind1], times[ind2]]
# found = False
# while not found:
#     t = [i + time for i in tinytimes]
#     if sum([t[i] % tinybus[i] for i in range(len(tinybus))]) == 0:
#         newtime = time  # store the largest pairwise solution to increment by
#         found = True
#     time += x1
# # now solve all of them using that newtime increment
# found = False
# while not found:
#     t = [i + time for i in times]
#     if sum([t[i] % bus[i] for i in range(len(bus))]) == 0:
#         print(time)
#         found = True
#     time += newtime


# Attempt 3
# still not nearly fast enough. but we could use that idea of stacking the solutions for each consecutive problem
# and solve them one at a time using the numbers (time and increment) for previous solves
# each one must solve to 0 for the time+its offset mod the bus number
# HINT: the increment will be a multiple of the bus number each time
inc = 1  # start incrementing at 1, but later increment by multiples of bus number
time = 0  # inside the loop, we keep the time because we know it must be larger
for each in range(len(bus)):
    found = False
    while not found:
        t = times[each] + time
        if t % bus[each] != 0:  # if we haven't found it yet
            time += inc  # look for the next multiple given our current time
        else:  # when we do find it
            inc = inc * bus[each]  # our increment going forward will now be a multiple of that bus number
            found = True
print(time)
