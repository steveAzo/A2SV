# Problem: Reduce Array Size to Half - https://leetcode.com/problems/reduce-array-size-to-the-half/

from collections import Counter

class Solution(object):
    def minSetSize(self, arr):
        n = len(arr)
        freqs = list(Counter(arr).values())
        freqs.sort(reverse=True)
        count = 0

        for freq in freqs:
            if n <= len(arr)//2:
                return count

            count += 1
            n -= freq
        
        return count
        