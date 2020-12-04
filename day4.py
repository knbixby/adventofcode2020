import csv
import re

# Part 1
# all passport entries need:
# byr
# iyr
# eyr
# hgt
# hcl
# ecl
# pid
# optional: cid

data = []
with open("day4.txt", 'r') as f:
    r = csv.reader(f)
    for row in r:
        data.append(row)

passports = {}
person = 0
passport = {}
for row in data:
    if not row:
        person += 1
        passports[person] = passport
        passport = {}
    else:
        items = row[0].split(" ")
        for each in items:
            entry = each.split(":")
            passport[entry[0]] = entry[1]
person += 1
passports[person] = passport

count = 0
required = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
for person in passports:
    if required.issubset(set(passports[person].keys())):
        count += 1
print(count)


# Part 2
# byr(Birth Year) - four digits; at least 1920 and at most 2002.
# iyr(Issue Year) - four digits; at least 2010 and at most 2020.
# eyr(Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt(Height) - a number followed by either cm or in: If cm, 150-193. If in, 59-76.
# hcl(Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl(Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid(Passport ID) - a nine - digit number, including leading zeroes.

count = 0
required = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
for person in passports:
    if required.issubset(set(passports[person].keys())):
        # more requirements
        if re.search("^\d{4}$", passports[person]["byr"]) and 1919 < int(passports[person]["byr"]) < 2003:
            if re.search("^\d{4}$", passports[person]["iyr"]) and 2009 < int(passports[person]["iyr"]) < 2021:
                if re.search("^\d{4}$", passports[person]["eyr"]) and 2019 < int(passports[person]["eyr"]) < 2031:
                    if re.search("^\d*(cm|in)", passports[person]["hgt"]):
                        num, system = int(passports[person]["hgt"][:-2]), passports[person]["hgt"][-2:]
                        if (system == "cm" and 149 < num < 194) or (system == "in" and 58 < num < 77):
                            if re.search("^#[\da-f]{6}$", passports[person]["hcl"]):
                                if re.search("^(amb|blu|brn|gry|grn|hzl|oth)$", passports[person]["ecl"]):
                                    if re.search("^\d{9}$", passports[person]["pid"]):
                                        count += 1
print(count)
