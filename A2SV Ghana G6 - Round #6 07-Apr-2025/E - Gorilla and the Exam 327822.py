# Problem: E - Gorilla and the Exam - https://codeforces.com/gym/601409/problem/E

def gorillaExam(n, k, a):
    a.sort()
    freq = []
    for i in range(n):
        if i > 0 and a[i] == a[i - 1]:
            freq[len(freq) - 1] += 1
        else:
            freq.append(1)

    # hash_map = {}
    # for i in range(n):
    #     if a[i] in hash_map:
    #         hash_map[a[i]] += 1
    #     else:
    #         hash_map[a[i]] = 1
        
    # freq = list(hash_map.values())
    freq.sort()
    i = 0
    while k > 0 and i < len(freq) - 1:
        if freq[i] <= k:
            k -= freq[i]
            i += 1
        else:
            break

    return len(freq) - i


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(gorillaExam(n, k, a))
