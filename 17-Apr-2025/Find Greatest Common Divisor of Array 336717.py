# Problem: Find Greatest Common Divisor of Array - https://leetcode.com/problems/find-greatest-common-divisor-of-array/

class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = max(nums)
        b = min(nums)

        while b != 0:
            a, b = b, a%b
        
        return abs(a)
        