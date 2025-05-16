# Problem: Capacity To Ship Packages Within D Days - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # weights.sort()

        left, right = max(weights), sum(weights)
        while left < right:
            capacity = (left + right) // 2
            days_required = 0
            curr_weight = 0
            for w in weights:
                curr_weight += w
                if curr_weight > capacity:
                    days_required += 1
                    curr_weight = w
                
            days_required += (curr_weight + capacity - 1) // capacity

            if days_required <= days:
                right = capacity
            else:
                left = capacity + 1
            
        return left
            
