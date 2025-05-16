# Problem: Koko Eating Bananas - https://leetcode.com/problems/koko-eating-bananas/

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Get the range for k
        # (Reduces the whole problem to a binary search space)
        # So that I will take the middle -th k, then do a linear traversal to know 
        # if I am hitting below the expected hours or not

        # Time Complexity O(nlogn)
        # logn for adjusting to find the correct k and for every possible k,
        # I do O(n) traversal to get the total number of hours it will take me

        left, right = 1, max(piles)
        while left < right:
            k = (left + right) // 2
            hours_req = 0
            for pile in piles:
                hours_req += (pile + k - 1) // k
            
            if hours_req <= h:
                right = k
            else:
                left = k + 1

        return left 