# Problem: Merge Sorted Array
(Easy) - https://leetcode.com/problems/merge-sorted-array/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_copy = nums1.copy()
        left, right = 0, 0
        iterator = 0
        m = len(nums1) - len(nums2)
        n = len(nums2)
        while left < m and right < n:
            if nums1_copy[left] < nums2[right]:
                nums1[iterator] = nums1_copy[left]
                left += 1
            else:
                nums1[iterator] = nums2[right]
                right += 1
            iterator += 1
        
        while left < m:
            nums1[iterator] = nums1_copy[left]
            left += 1
            iterator += 1
        
        while right < n:
            nums1[iterator] = nums2[right]
            right += 1
            iterator += 1
        
        