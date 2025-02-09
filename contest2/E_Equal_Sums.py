def equalSums(test_cases):
    hash_map = {}
    
    for seq_id in range(test_cases):
        s_length = int(input())
        s = list(map(int, input().split()))
        total = sum(s)
        for i in range(s_length):
            total_i = total - s[i]
            if total_i in hash_map:
                prev_seq_id, prev_i = hash_map[total_i]
                if seq_id + 1 != prev_seq_id:
                    print("YES")
                    print(prev_seq_id, prev_i)
                    print(seq_id + 1, i + 1)
                    exit()
            else:
                hash_map[total_i] = (seq_id + 1, i + 1)
    print("NO")

test_cases = int(input())
equalSums(test_cases)


