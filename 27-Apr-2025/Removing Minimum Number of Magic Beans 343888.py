# Problem: Removing Minimum Number of Magic Beans - https://leetcode.com/problems/removing-minimum-number-of-magic-beans/

class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        beans.sort()

        prefix = [0] * len(beans)
        prefix[0] = beans[0]
        for i in range(1, len(beans)):
            prefix[i] = prefix[i-1] + beans[i]
        print(prefix)

        beans_count = 0
        min_count = float('inf')
        for i in range(len(beans)):
            drop_count = prefix[i - 1] if i > 0 else 0
            add_up = (prefix[-1] - prefix[i]) - beans[i] * (len(beans) - i - 1)
            
            beans_count = drop_count + add_up
            min_count = min(min_count, beans_count)
        
        return min_count