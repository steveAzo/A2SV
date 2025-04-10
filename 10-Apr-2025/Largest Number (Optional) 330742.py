# Problem: Largest Number (Optional) - https://leetcode.com/problems/largest-number/

class Solution(object):
    def largestNumber(self, nums):
        res = [str(i) for i in nums]
        for i in range(1, len(nums)):
            j = i
            while j > 0 and res[j] + res[j-1] > res[j-1] + res[j]:
                res[j], res[j-1] = res[j-1], res[j]
                j -= 1
        
        result = ''.join(res)

        if int(result) == 0:
            return '0'
        else:
            return result
        