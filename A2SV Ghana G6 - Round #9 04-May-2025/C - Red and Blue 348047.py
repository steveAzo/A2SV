# Problem: C - Red and Blue - https://codeforces.com/gym/606423/problem/C

t = int(input())
for _ in range(t):
    n = int(input())
    r = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))

    prefix_max_r = 0
    prefix_r = 0
    for i in range(n):
        prefix_r += r[i]
        prefix_max_r = max(prefix_max_r, prefix_r)
    
    prefix_max_b = 0
    prefix_b = 0
    for j in range(m):
        prefix_b += b[j]
        prefix_max_b = max(prefix_max_b, prefix_b)
    
    res = prefix_max_b + prefix_max_r
    print(res)

