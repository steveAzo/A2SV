# Problem: Find Unique Binary String - https://leetcode.com/problems/find-unique-binary-string/description/

class Solution(object):
    def findDifferentBinaryString(self, nums):
        n = len(nums[0])

        decimal = [int(num, 2) for num in nums]
        for i in range(2**n + 1):
            if i not in decimal:
                return bin(i)[2:].zfill(n)