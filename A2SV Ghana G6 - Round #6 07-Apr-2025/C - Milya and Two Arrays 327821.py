# Problem: C - Milya and Two Arrays - https://codeforces.com/gym/601409/problem/C

def mergeArray(a, b):
    dist_a = len(set(a))
    dist_b = len(set(b))

    if dist_a * dist_b >= 3:
        return "YES"
    else:
        return "NO"

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(mergeArray(a, b))