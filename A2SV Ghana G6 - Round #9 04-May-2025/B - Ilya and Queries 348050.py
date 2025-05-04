# Problem: B - Ilya and Queries - https://codeforces.com/gym/606423/problem/B


def queries(prefix, a, b):
    return prefix[b - 1] - prefix[a - 1]

def preprocess(s):
    prefix = [0] * len(s)
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            prefix[i] = prefix[i - 1] + 1
        else:
            prefix[i] = prefix[i - 1]
    return prefix

s = input()
prefix = preprocess(s)
m = int(input())
for _ in range(m):
    l, r = map(int, input().split())
    print(queries(prefix, l, r))