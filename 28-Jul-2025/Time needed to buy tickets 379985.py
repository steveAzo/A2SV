# Problem: Time needed to buy tickets - https://leetcode.com/problems/time-needed-to-buy-tickets/

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        # simulation approach
        seconds = 0
        while tickets[k] > 0:
            for i in range(len(tickets)):
                if tickets[k] == 0:
                    return seconds
                
                if tickets[i] == 0:
                    continue
                
                seconds += 1
                tickets[i] -= 1
        
        return seconds