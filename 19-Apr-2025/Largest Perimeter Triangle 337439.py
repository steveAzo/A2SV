# Problem: Largest Perimeter Triangle - https://leetcode.com/problems/largest-perimeter-triangle/

class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        end, l, r = len(nums) - 1, len(nums) - 3, len(nums) -2
        if nums[r] + nums[l] > nums[end]:
                return nums[r] + nums[l] + nums[end]

        max_perimeter = 0
        while l > - 1:
            if nums[r] + nums[l] > nums[end]:
                return nums[r] + nums[l] + nums[end]
            
            if nums[r] + nums[l] <= nums[end]:
                l -= 1
                r -= 1
                end -= 1

        return max_perimeter
        