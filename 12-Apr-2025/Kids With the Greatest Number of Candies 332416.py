# Problem: Kids With the Greatest Number of Candies - https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        res = []
        max_val = max(candies)

        for i in range(len(candies)):
            if candies[i] + extraCandies >= max_val:
                res.append(True)
            else:
                res.append(False)
        
        return res

        