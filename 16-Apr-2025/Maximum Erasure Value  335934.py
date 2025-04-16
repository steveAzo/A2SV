# Problem: Maximum Erasure Value  - https://leetcode.com/problems/maximum-erasure-value/

class Solution(object):
    def maximumUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        num_dict = defaultdict(int)
        start = 0
        end = 0
        max_sum = 0
        sum_ = 0
        while end < len(nums):
            num_dict[nums[end]] += 1
            if num_dict[nums[end]] > 1:
                max_sum = max(max_sum, sum_)

            sum_ += nums[end]

            while num_dict[nums[end]] > 1:
                sum_ -= nums[start]
                num_dict[nums[start]] -= 1
                start += 1

            end += 1
        max_sum = max(max_sum, sum_)
        
        return max_sum 