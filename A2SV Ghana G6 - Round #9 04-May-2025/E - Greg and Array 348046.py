# Problem: E - Greg and Array - https://codeforces.com/gym/606423/problem/E

n, m, k = map(int, input().split())
a = list(map(int, input().split()))
a.append(0)
operations = []
for _ in range(m):
    b = list(map(int, input().split()))
    operations.append(b)

queries = []
for _ in range(k):
    query = list(map(int, input().split()))
    queries.append(query)

op_prefix = [0] * (len(operations) + 1)
for query in queries:
    op_prefix[query[0] - 1] += 1
    op_prefix[query[1]] -= 1

total = 0
for i in range(len(op_prefix)):
    total += op_prefix[i]
    op_prefix[i] = total

res = [0] * (n + 1)
for i in range(len(operations)):
    op = operations[i]
    res[op[0] - 1] += (op_prefix[i] * op[2])
    res[op[1]] -= (op_prefix[i] * op[2])

tot = 0
for i in range(n):
    tot += res[i]
    a[i] += tot
a.pop()
print(*a)