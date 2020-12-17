import csv

data = []
with open("day16.txt", 'r') as f:
    r = csv.reader(f)
    for row in r:
        data.append(row)

ruls = data[:20]
ticket = data[22]
tix = data[25:]

rules = {}
for rule in ruls:
    name = rule[0].split(":")
    rules[name[0]] = {}
    nums = name[1].strip().split(" or ")
    for i, each in enumerate(nums):
        n = each.split("-")
        rules[name[0]][i] = (int(n[0]), int(n[1]))


# for all the rules in our rule dictionary, which values exist completely outside the rules?
# then search tickets for them and add up all those values

# no value is greater than three digits:
print(set([len(each) for row in tix for each in row]))

vals = range(1000)
valid = []
for r in rules:
    for each in rules[r]:
        valid += range(rules[r][each][0], rules[r][each][1]+1)

invalid = set(vals) - set(valid)

errors = []
badrow = []
for i, row in enumerate(tix):
    for each in row:
        if int(each) in invalid:
            errors.append(int(each))
            badrow.append(i)
print(sum(errors))

# update our ticket set with only the good ones
goodtix = [row for i, row in enumerate(tix) if i not in badrow]

# for goodtix, figure out which rule applies to the numbers in the column to match each column with its data field
# after matched, take all columns whose name starts with departure and multiply their values on my ticket

# for each column, get the set of numbers in it, and compare with the set of numbers that satisfy every rule.
match = {}
for col in range(len(goodtix[0])):
    colset = set([int(row[col]) for row in goodtix])
    rule = []  # list of all rules that match the column's values
    for r in rules:
        rulerange = []
        for i in rules[r]:
            rulerange += range(rules[r][i][0], rules[r][i][1]+1)
        ruleset = set(rulerange)
        if colset.issubset(ruleset):
            rule.append(r)
    match[col] = rule

# only one column satisfies just 1 rule; use that to narrow down subsequent columns to their actual rule
rem = "arrival station"
for i in range(len(match)):
    for each in match:
        if len(match[each]) > 1:
            if rem in match[each]:
                newmatch = match[each]
                newmatch.remove(rem)
                if len(newmatch) == 1:
                    nextrem = newmatch  # not a good idea but it works for this
                match[each] = newmatch
    rem = nextrem[0]

inds = []
for each in match:
    if "departure" in match[each][0]:
        inds.append(each)

mine = [int(ticket[i]) for i in inds]

i = 1
for each in mine:
    i *= each
print(i)
