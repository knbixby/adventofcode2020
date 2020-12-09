import csv

data = []
with open("day8.txt", 'r') as f:
    r = csv.reader(f, delimiter="\t")
    for row in r:
        data.append(row)


# Part 1
# acc number changes the counter by the amount
# nop does nothing
# jmp changes the line of the code we're at

# split data into commands and numbers
gamecode = [row[0].split(" ") for row in data]
for row in gamecode:
    row[1] = int(row[1])

executed = []  # a list of the lines of code we've already executed
count = 0  # the number we're at from "acc" commands
i = 0
# if a line of executed code is seen again, print count and end execution
while i != len(gamecode):
    if i not in executed:
        executed.append(i)
        c = gamecode[i][0]
        if c == "nop":
            i += 1
        elif c == "acc":
            count += gamecode[i][1]
            i += 1
        elif c == "jmp":
            i += gamecode[i][1]
        else:
            print("error")
    else:
        print(count)
        break


# Part 2
# get indices of commands to change
switch = [i for i, row in enumerate(gamecode) if (row[0] == "nop" or row[0] == "jmp")]

for game in range(len(switch)):  # how many games we need to try to see if we run the final line of code
    gamecode[switch[game]][0] = "jmp" if gamecode[switch[game]][0] == "nop" else "nop"
    executed = []  # a list of the lines of code we've already executed
    count = 0  # the number we're at from "acc" commands
    i = 0
    finished = False  # stop when we're done
    while i != len(gamecode):
        if i not in executed:
            executed.append(i)
            c = gamecode[i][0]
            if c == "nop":
                i += 1
            elif c == "acc":
                count += gamecode[i][1]
                i += 1
            elif c == "jmp":
                i += gamecode[i][1]
            else:
                print("error")
        else:
            gamecode[switch[game]][0] = "nop" if gamecode[switch[game]][0] == "jmp" else "jmp"  # change back; try again
            break
        if i == len(gamecode)-1:
            print(count)
            finished = True
    if finished:
        break
