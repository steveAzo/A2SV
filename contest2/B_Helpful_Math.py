def summation(s):
    s = s.split('+')
    s.sort()

    return '+'.join(s)

s = input()
print(summation(s))
