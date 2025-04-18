# Problem: Number of Subarrays With GCD Equal to K - https://leetcode.com/problems/number-of-subarrays-with-gcd-equal-to-k/description/

class Solution(object):
    def subarrayGCD(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        for i in range(len(nums)):
            current_gcd = nums[i]
            for j in range(i, len(nums)):
                current_gcd = self.gcd(current_gcd, nums[j])
                if current_gcd < k:
                    break
                if current_gcd == k:
                    count += 1
        
        return count

    def gcd(self, a, b):
        a, b = max(a, b), min(a, b)
        while b != 0:
            a, b = b, a%b
        return abs(a)
        