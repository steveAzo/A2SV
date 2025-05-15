# Problem: H-Index - https://leetcode.com/problems/h-index/

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        max_h_index = 0
        n = len(citations)

        citations.sort()
        for i in range(n):
            current_max_poss_h_index = min(n - i, citations[i])
            max_h_index = max(max_h_index, current_max_poss_h_index)

        return max_h_index