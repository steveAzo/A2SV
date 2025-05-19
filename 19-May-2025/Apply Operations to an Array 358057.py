# Problem: Apply Operations to an Array - https://leetcode.com/problems/apply-operations-to-an-array/

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] = nums[i] * 2
                nums[i + 1] = 0
        # print(nums)

        seeker, finder = 0, 0
        while finder < len(nums):
            if nums[finder] != 0:
                nums[seeker], nums[finder] = nums[finder], nums[seeker]
                seeker += 1
            finder += 1
        
        return nums
