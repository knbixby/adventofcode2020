import csv

data = []
with open("day9.txt", 'r') as f:
    r = csv.reader(f, delimiter="\t")
    for row in r:
        data.append(int(row[0]))


# Part 1
# first number in list which is not a sum of previous 25 numbers (starting with item 26)
def isSum(target, nums):
    nums.sort()
    nums = [i for i in nums if i < target]  # throw out numbers larger than target
    for num in nums:
        if target-num in nums:
            return True
    return False

invalid = 0
for i, num in enumerate(data):
    if i > 24:
        ans = isSum(data[i], data[i-25:i])
        if not ans:
            invalid = data[i]
            print(invalid)
            break


# Part 2
# using invalid number, find run of numbers that sum to invalid number, then return sum of first/last of the run
for i, num in enumerate(data):
    total = num
    index = i
    while total < invalid:
        index += 1
        total += data[index]
    if total == invalid:
        run = data[i:index+1]
        print(min(run) + max(run))
        break
