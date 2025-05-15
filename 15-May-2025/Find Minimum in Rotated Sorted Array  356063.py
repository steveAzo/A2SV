# Problem: Find Minimum in Rotated Sorted Array  - https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            # if mid == 0 or mid == len(nums) - 1:
            #     return nums[mid]
            
            if nums[right] > nums[mid] and nums[mid] > nums[left]:
                return nums[left]
            
            if nums[mid] < nums[mid + 1] and nums[mid-1] > nums[mid]:
                return nums[mid]
            
            if nums[right] > nums[mid]:
                right = mid
            else:
                left = mid + 1

        return nums[left]