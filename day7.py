import csv
import re

data = []
with open("day7.txt", 'r') as f:
    r = csv.reader(f, delimiter="\t")
    for row in r:
        data.append(row)

# turn the rules data into a dictionary where each bag is listed with rules (required bag type: required bag amount)
rules = {}
for row in data:
    contents = {}
    s = row[0].split("contain")  # separate each bag from its required contents
    container, content = s[0].strip(), s[1]
    content = re.sub("\sno\s", " 0 ", content)  # 0 is represented with text; turn into number
    for each in content.split(","):  # each required bag type separated with comma
        contents[re.sub("\d+", "", each).strip(". ").rstrip("s")] = re.search("\d+", each).group()  # remove plurals
    rules[container.rstrip("s")] = contents  # remove plurals; assign each bag its required contents


# Part 1
# recursion: how many bags may contain a shiny gold bag?
def searchbags(target, targets, d):
    for each in d:
        if target in d[each] and each not in targets:
            targets.append(each)
            searchbags(each, targets, d)
    return targets
total = searchbags("shiny gold bag", [], rules)
print(len(total))


# Part 2
# starting with shiny gold bag, how many bags must fit inside that bag?
targets = ["shiny gold bag"]
for each in targets:
    for bag in rules[each]:
        targets.extend([bag]*int(rules[each][bag]))
print(len(targets[1:]))  # we don't count our original gold bag
