import time

# read in the data
data = []
with open("day1.txt", 'rU') as f:
    for row in f:
        data.append(int(row))

target = 2020  # desired sum

# Part 1
# find the two numbers in the data that sum to 2020, then multiply them together

tic = time.time()
for i in range(len(data)-1):
    for j in range(i+1,len(data)):
        if data[i] + data[j] == target:
            print("%d * %d = %d" % (data[i], data[j], data[i] * data[j]))
            break
# answer: 492, 1528, product 751776
toc = time.time()
print((toc-tic)/1000.0)

# second method to solve part 1 (unnecessarily optimized)
tic = time.time()
data.sort()
# pick first number and go in the middle, then in direction of 2020 until you reach or pass it, then stop
center = len(data)/2
stop = False
for i in range(len(data)):
    if stop:
        break
    if data[i] + data[center] > target:
        # go backwards until <= target
        for j in reversed(range(center)):
            if data[i] + data[j] == target:
                print(data[i]*data[j])
                stop = True
                break
            elif data[i] + data[j] < target:
                break
    elif data[i] + data[center] < target:
        # go forwards until >= target
        for j in range(center, len(data)):
            if data[i] + data[j] == target:
                print(data[i]*data[j])
                stop = True
                break
            elif data[i] + data[j] > target:
                break
    else:
        print(data[i]*data[center])
        stop = True
        break
toc = time.time()
print((toc - tic) / 1000.0)


# Part 2
# now find the three numbers in the data that sum to 2020, then multiply them together
stop = False
tic = time.time()
for i in range(len(data)-2):
    for j in range(i+1, len(data)-1):
        if stop:
            break
        for k in range(i+2, len(data)):
            if data[i] + data[j] + data[k] == target:
                print("%d * %d * %d = %d" % (data[i], data[j], data[k], data[i] * data[j] * data[k]))
                stop = True
                break
# answer: 1258, 47, 715, product 42275090
toc = time.time()
print((toc - tic) / 1000.0)

# second method to solve part 2
tic = time.time()
# just stop after you pass 2020, nothing fancier
data.sort()  # redundant, data already sorted above
stop = False
for i in range(len(data)-2):
    for j in range(i+1, len(data)-1):
        if stop or (data[i]+data[j] > target):
            break
        for k in range(i+2, len(data)):
            if data[i]+data[j]+data[k] > target:
                break
            if data[i] + data[j] + data[k] == target:
                print("%d * %d * %d = %d" % (data[i], data[j], data[k], data[i] * data[j] * data[k]))
                stop = True
                break
toc = time.time()
print((toc - tic) / 1000.0)
