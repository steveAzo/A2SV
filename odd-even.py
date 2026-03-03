n = int(input())
a = list(map(int, input().split()))

has_odd = False 
has_even = False

for i in range(n):
    if a[i] % 2 == 0:
        has_even = True 
    
    if a[i] % 2 != 0:
        has_odd = True 

if has_even and has_odd:
    a.sort()
    print(*a)
else:
    print(*a) 
