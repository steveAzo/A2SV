def numberSmaller(n, m, a, b):
    i = 0 
    j = 0
    res = []
    while i < m:
        while j < n and a[j] < b[i]:
            j += 1
        res.append(j)
        i += 1
    
    return res 


n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split())) 
print(*numberSmaller(n, m, a, b))
