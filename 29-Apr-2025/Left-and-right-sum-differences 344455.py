# Problem: Left-and-right-sum-differences - https://leetcode.com/problems/left-and-right-sum-differences/

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        if not nums:
            return 0

        left_prefix = [0] * len(nums)
        right_prefix = [0] * len(nums)

        total = 0
        for i in range(1, len(nums)):
            total += nums[i-1]
            left_prefix[i] = total

        total_ = 0
        for j in range(len(nums) - 2, - 1, - 1):
            total_ += nums[j + 1]
            right_prefix[j] = total_

        return [abs(left_prefix[i] - right_prefix[i]) for i in range(len(nums))]
