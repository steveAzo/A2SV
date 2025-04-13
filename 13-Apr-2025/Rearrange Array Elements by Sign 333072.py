# Problem: Rearrange Array Elements by Sign - https://leetcode.com/problems/rearrange-array-elements-by-sign/description/

from itertools import zip_longest

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive_array = []
        negative_array = []
        resulting_array = []

        for i in range(len(nums)):
            if nums[i] < 0:
                negative_array.append(nums[i])
            else:
                positive_array.append(nums[i])
        
        for p, n in zip_longest(positive_array, negative_array, fillvalue=''):
            resulting_array.append(p)
            resulting_array.append(n)
        return resulting_array

        