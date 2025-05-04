# Problem: A - Promo - https://codeforces.com/gym/606423/problem/A


n, q = map(int, input().split())
p = list(map(int, input().split()))
p.sort(reverse=True)
prefix = [0] * (len(p) + 1)
total = 0
for j in range(len(p)):
    total += p[j]
    prefix[j] = total
for _ in range(q):  
    x, y = map(int, input().split())
    res = prefix[x-1] - prefix[x-y-1]
    print(res)
