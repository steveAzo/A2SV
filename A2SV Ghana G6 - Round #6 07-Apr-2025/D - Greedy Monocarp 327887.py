# Problem: D - Greedy Monocarp - https://codeforces.com/gym/601409/problem/D

def greedyMonocarp(n, k, a):
    a.sort(reverse=True)

    total = 0
    i = 0
    while i < n:
        if total + a[i] > k:
            return k - total
        elif total + a[i] == k:
            return 0
        else:
            total += a[i] 
        i += 1
    
    if total < k:
        return k - total


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split())) 
    print(greedyMonocarp(n, k, a))