data = [11, 0, 1, 10, 5, 19]


# took me way too long to understand the rules.

# originally i was storing the game, but it's not possible to do that for 30m rounds.* since all we care about is the
# previous number and if/where it appeared in the game earlier, just store the previous number and those indices
# * even with pre-allocation, which i ill-advisedly tried

# also originally i stored all indices of a given number in the `said` dictionary but again that's unnecessary and
# quickly became unwieldy. since i only need to know the previous number's index and its most recent prior index, just
# stored as tuple in the dict (though figuring out when to update that was annoying)


# Part 1
def play(data, howmany):
    said = {}
    for i, start in enumerate(data):
        said[start] = (i, i)  # ok to default like so, as the 2nd appearance updates 2nd index before distance calc
    prev = data[-1]

    for i in range(len(data), howmany):  # start where we left off in the game
        if prev not in said:  # checking adds it to our dict but that's ok bc we immediately add the initial index value
            said[prev] = (i-1, i-1)
            prev = 0
        else:
            said[prev] = (said[prev][1], i-1)
            prev = said[prev][1] - said[prev][0]
    return(prev)


play(data, 2020)


# Part 2
play(data, 30000000)
