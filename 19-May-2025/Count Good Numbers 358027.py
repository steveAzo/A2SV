# Problem: Count Good Numbers - https://leetcode.com/problems/count-good-numbers/

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        def helper(base, exp):
            result = 1
            while exp > 0:
                if exp & 1:
                    result = (result * base) % MOD
                
                exp >>= 1
                base = (base * base) % MOD
            
            return result
        
        odd_indices = n//2
        even_indices = (n+1)//2

        return (helper(5, even_indices) * helper(4, odd_indices)) % MOD