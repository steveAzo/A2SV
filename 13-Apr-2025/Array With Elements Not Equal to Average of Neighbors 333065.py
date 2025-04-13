# Problem: Array With Elements Not Equal to Average of Neighbors - https://leetcode.com/problems/array-with-elements-not-equal-to-average-of-neighbors/

class Solution(object):
    def rearrangeArray(self, nums):
        nums.sort()
        median = None
        if len(nums)%2 == 1:
            median = nums[len(nums)//2] 
        else:
            median = (nums[len(nums)//2] + nums[len(nums)//2 - 1]) / 2.0
        
        res = [0]*len(nums)
        even_idx = 0
        odd_idx = 1
        for i in range(len(nums)):
            if nums[i] < median and odd_idx < len(nums):
                res[odd_idx] = nums[i]
                odd_idx += 2
            elif nums[i] >= median and even_idx <len(nums):
                res[even_idx] = nums[i]
                even_idx += 2
        return res