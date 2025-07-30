# Problem: Next Greater Element - https://leetcode.com/problems/next-greater-element-i/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater_hash = {num : -1 for num in nums2}

        stack = []
        for i in range(len(nums2)):
            while stack and nums2[i] > nums2[stack[-1]]:
                idx = stack.pop()
                next_greater_hash[nums2[idx]] = i
            else:
                stack.append(i)
        
        res = [-1] * len(nums1)
        for j in range(len(nums1)):
            idx = next_greater_hash[nums1[j]]
            if idx != -1:
                res[j] = nums2[idx]
        
        return res


