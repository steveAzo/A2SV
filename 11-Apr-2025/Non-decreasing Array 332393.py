# Problem: Non-decreasing Array - https://leetcode.com/problems/non-decreasing-array/

class Solution(object):
    def checkPossibility(self, nums):
        count = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                count += 1

                if count >=2:
                    return False

                if i == 0 or nums[i-1] <= nums[i+1]:
                    nums[i] = nums[i+1]
                else:
                    nums[i+1] = nums[i]

            
        return True
        