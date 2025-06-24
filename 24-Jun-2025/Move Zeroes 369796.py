# Problem: Move Zeroes - https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        placeholder = 0
        for finder in range(len(nums)):
            if nums[finder] != 0:
                nums[placeholder], nums[finder] = nums[finder], nums[placeholder]
                placeholder += 1
        
        
        