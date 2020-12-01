# read in the data
data = []
with open("day1.txt", 'rU') as f:
    for row in f:
        data.append(int(row))

# Part 1
# find the two numbers in the data that sum to 2020, then multiply them together

for i in range(len(data)-1):
    for j in range(i+1,len(data)):
        if data[i] + data[j] == 2020:
            print("%d * %d = %d" % (data[i], data[j], data[i] * data[j]))
            break
# answer: 492, 1528, product 751776)

# Part 2
# now find the three numbers in the data that sum to 2020, then multiply them together
stop = False
for i in range(len(data)-2):
    for j in range(i+1, len(data)-1):
        if stop:
            break
        for k in range(i+2, len(data)):
            if data[i] + data[j] + data[k] == 2020:
                print("%d * %d * %d = %d" % (data[i], data[j], data[k], data[i] * data[j] * data[k]))
                stop = True
                break
# answer: 1258, 47, 715, product 42275090)
