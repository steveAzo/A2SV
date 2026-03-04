n, m = list(map(int, input().split()))
a = list(map(int, input().split())) 
b = list(map(int, input().split())) 

p1, p2 = 0, 0 
res = []
while p1 < n and p2 < m:
    if a[p1] < b[p2]:
        res.append(a[p1])
        p1 += 1
    else:
        res.append(b[p2])
        p2 += 1 

if p1 < n:
    res.extend(a[p1:])
if p2 < m:
    res.extend(b[p2:])

print(*res)
