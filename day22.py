import csv

data = []
with open("day22.txt", 'r') as f:
    r = csv.reader(f)
    for row in r:
        data.append(row)

p1 = [int(i[0]) for i in data[1:26]]
p2 = [int(i[0]) for i in data[28:]]


# Part 1
def play(d1, d2):
    c1 = d1[0]
    c2 = d2[0]
    if c1 > c2:
        d1 = d1[1:] + [c1, c2]
        d2 = d2[1:]
    else:
        d1 = d1[1:]
        d2 = d2[1:] + [c2, c1]
    return(d1, d2)

while p1 and p2:
    p1, p2 = play(p1, p2)

c = 0
if p1:
    p1.reverse()
    for i, num in enumerate(p1):
        c += (i+1) * num
elif p2:
    p2.reverse()
    for i, num in enumerate(p2):
        c += (i+1) * num

print(c)


# Part 2

# 1. within a game, if the same players had the same hands, player1 wins and game ends

# 2. the card each player draws must have lower or equal value to the number of cards remaining in their deck
#    if so, start a game of recursive combat

# 3. if one or both players draws a card of higher value than the remaining number of cards in the deck,
#    it's a regular game: normal rules like above

# 4. recursive games are:
#    each player pretend-draws the number of cards listed on their drawn card and plays a separate game
#    the winner wins the original round and the cards are added to their deck with winner's card first

# there can be games within games
# there's no way the crab can play this game. not even humans could. no offense to crabs!


def playwar(d1, d2):
    games = set()  # originally had stored the tuples of each player's deck in a dictionary as a list with the key
    # being the first two cards but that was overcomplicated

    while d1 and d2:
        c1 = d1.pop(0)
        c2 = d2.pop(0)

        if (tuple(d1), tuple(d2)) in games:
            return(1, d1)
        else:
            games.add((tuple(d1), tuple(d2)))

        if (c1 <= len(d1)) and (c2 <= len(d2)):
            # play recursive war
            w, _ = playwar(d1[:c1], d2[:c2])
        else:
            if c1 > c2:
                w = 1
            else:
                w = 2
        if w == 1:
            d1 += [c1, c2]
        else:
            d2 += [c2, c1]
    if d1:
        w = 1
        deck = d1
    else:
        w = 2
        deck = d2
    return(w, deck)

# p1 = [9, 2, 6, 3, 1]  # debugging
# p2 = [5, 8, 4, 7, 10]
p1 = [int(i[0]) for i in data[1:26]]
p2 = [int(i[0]) for i in data[28:]]

winner, deck = playwar(p1, p2)

c = 0
deck.reverse()
for i, num in enumerate(deck):
    c += (i+1) * num

print(c)
