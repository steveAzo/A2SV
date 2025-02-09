
def perfectSquare(n, a):
    a = [int(i) for i in a]

    max_largest = float('-inf')
    for num in a:
        if num < 0:
            max_largest = max(max_largest, num)
        else:
            root = int(num**(0.5))
            if num != root**2:
                max_largest = max(max_largest, num)

    return max_largest if max_largest != float('-inf') else None

n = int(input())
a = input().split()
print(perfectSquare(n, a))