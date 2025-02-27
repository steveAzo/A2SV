# Problem: Merge Strings Alternately - https://leetcode.com/problems/merge-strings-alternately/

from itertools import zip_longest

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ''

        for char1, char2 in zip_longest(word1, word2, fillvalue=''):
            result += char1 + char2
        
        return result
        