# Problem: Longest Palindrome - https://leetcode.com/problems/longest-palindrome/

class Solution:
    def longestPalindrome(self, s: str) -> int:
        hash_map = {}
        for i in range(len(s)):
            if s[i] in hash_map:
                hash_map[s[i]] += 1
            else:
                hash_map[s[i]] = 1
        
        count = 0
        has_mid = False
        for num in hash_map.values():
            has_mid = has_mid or num % 2 == 1
            count += 2 * (num // 2)

        return count + has_mid
            
        