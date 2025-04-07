# Problem: B - Was there an Array? - https://codeforces.com/gym/601409/problem/B

def equality(n, b):
    if len(b) < 3:
        return "YES"
    
    for i in range(len(b) - 2):
        if b[i] == 1 and b[i + 1] == 0 and b[i + 2] == 1:
            return "NO"
        
    return "YES"

t = int(input())     
for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    print(equality(n, b))
