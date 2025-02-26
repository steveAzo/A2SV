# Problem: Watermelon - https://codeforces.com/problemset/problem/4/A

def printOut(n):
    if n <= 2:
        print("NO")
    elif n > 2:
        if n % 2 == 0:
            print("YES")
        else:
            print("NO")
 
n = int(input())
printOut(n)