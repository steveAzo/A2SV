# Problem: X of a Kind in a Deck of Cards - https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/

from collections import Counter

class Solution(object):
    def gcd(self, a, b):
        a, b = max(a, b), min(a, b)
        while b != 0:
            a, b = b, a%b
    
        return abs(a)

    def hasGroupsSizeX(self, deck):
        if len(deck) <= 1:
            return False

        hash_map = Counter(deck)
        res = list(hash_map.values())

        current_gcd = res[0]
        for i in range(1, len(res)):
            current_gcd = self.gcd(current_gcd, res[i])
            if current_gcd == 1:
                return False
            
        
        return current_gcd > 1