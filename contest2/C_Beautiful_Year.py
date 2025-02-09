def beautifulYear(y):
    y = y + 1
    if len(set(str(y))) >= 4:
        return y
    while len(set(str(y))) < 4:
        y += 1
    return y

y = int(input())
print(beautifulYear(y))