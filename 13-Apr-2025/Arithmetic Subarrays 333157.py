# Problem: Arithmetic Subarrays - https://leetcode.com/problems/arithmetic-subarrays/

class Solution(object):
    def checkArithmeticSubarrays(self, nums, l, r):
        res = [0]*len(l)
        for i in range(len(l)):
            sub = nums[l[i]:r[i]+1]
            sub.sort()
            res[i] = all(sub[i] - sub[i-1] == sub[1] - sub[0] for i in range(1, len(sub)))
        
        return res
        