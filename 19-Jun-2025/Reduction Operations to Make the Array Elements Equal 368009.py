# Problem: Reduction Operations to Make the Array Elements Equal - https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal/

class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        
        right = len(nums) - 1
        count = 0
        for left in range(len(nums) - 2, - 1, - 1):
            if nums[left] < nums[left + 1]:
                count += right - left
        
        return count