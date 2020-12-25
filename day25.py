card = 16616892
door = 14505727


def transform(num, times):
    num = pow(num, times, 20201227)
    return num

x = 0
while transform(7, x) != card:
    x += 1

print(pow(door, x, 20201227))
