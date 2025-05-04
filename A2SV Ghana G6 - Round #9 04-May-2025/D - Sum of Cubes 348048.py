# Problem: D - Sum of Cubes - https://codeforces.com/gym/606423/problem/D

def isPossible(x):
    for a in range(1, int(x**(1/3)) + 1):
        if a**3 > x:
            break
        
        diff = (x-a**3)
        b = round(diff**(1/3))
        if b**3 == diff and b > 0:
            return "YES"
    return "NO"

t = int(input())
for _ in range(t):
    x = int(input())
    print(isPossible(x))
