# Problem: Maximum Number of Coins You Can Get - https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

class Solution(object):
    def maxCoins(self, piles):
        piles.sort(reverse=True)

        total = 0
        left = 1
        right = len(piles) - 1
        while left < right:
            total += piles[left]
            left += 2
            right -= 1
            
        return total