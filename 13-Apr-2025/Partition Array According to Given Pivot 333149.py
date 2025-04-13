# Problem: Partition Array According to Given Pivot - https://leetcode.com/problems/partition-array-according-to-given-pivot/description/

class Solution(object):
    def pivotArray(self, nums, pivot):
        before_pivot = []
        after_pivot = []

        for i in range(len(nums)):
            if nums[i] < pivot:
                before_pivot.append(nums[i])
            elif nums[i] > pivot:
                after_pivot.append(nums[i])
        
        for j in range(len(before_pivot)):
            nums[j] = before_pivot[j]
        
        for m in range(len(nums) - (len(before_pivot) + len(after_pivot))):
            nums[len(before_pivot) + m] = pivot

        for k in range(len(after_pivot)):
            nums[len(nums) - len(after_pivot) + k] = after_pivot[k]
        
        return nums
        