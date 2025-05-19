# Problem: Replace Elements with Greatest Element on Right Side - https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = [-1] * len(arr)

        next_biggest = arr[-1]
        for i in range(len(arr) - 2, - 1, - 1):
            res[i] = next_biggest
            next_biggest = max(arr[i], next_biggest)
            
        return res