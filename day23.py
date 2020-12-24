data = "215694783"

c = [int(i) for i in data]

# Part 1
for x in range(100):
    cup = c[0]
    lift = c[1:4]
    # find the correct index to drop, while wrapping around...
    target = cup-1 if cup > 1 else 9
    while target in lift:
        target -= 1
        if target < 1:
            target = max(c)
    i = c.index(target)
    c = c[4:i+1] + lift + c[i+1:] + [cup]
    print(c)

mylist = c[c.index(1)+1:]+c[:c.index(1)]
mystr = [str(each) for each in mylist]
print("".join(mystr))


# Part 2

class Cup:
    def __init__(self, id):
        self.id = id
        self.next = None

# circular linked list
tot = 1000000
# new list
c = [int(i) for i in data] + [i for i in range(10, tot+1)]
cups = {}
for each in c:
    cups[each] = Cup(each)

for i, num in enumerate(c[:-1]):
    cups[num].next = cups[c[i+1]]
cups[c[-1]].next = cups[c[0]]

# # it worked!
# for each in cups:
#     print(cups[each].id, cups[each].next.id)

mycup = cups[c[0]]  # our starting cup
for x in range(10000000):
    c1, c2, c3 = mycup.next, mycup.next.next, mycup.next.next.next
    nums = [c1.id, c2.id, c3.id]

    # close the loop (the three cups are outside right now)
    mycup.next = mycup.next.next.next.next

    # find the new location according to the rules
    target = mycup.id-1 if mycup.id > 1 else tot
    while target in nums:
        target -= 1
        if target < 1:
            target = tot

    # open the loop and replace the three cups
    c3.next = cups[target].next
    cups[target].next = c1

    mycup = mycup.next

print(cups[1].next.id * cups[1].next.next.id)
