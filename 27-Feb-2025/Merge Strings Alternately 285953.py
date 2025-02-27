# Problem: Merge Strings Alternately - https://leetcode.com/problems/merge-strings-alternately/

class Solution(object):
    def mergeAlternately(self, word1, word2):
        result = ''

        i = 0
        j = 0
        while i < len(word1) and j < len(word2):
            result += word1[i]
            result += word2[j]
            i += 1
            j += 1
        while i < len(word1):
            result += word1[i]
            i += 1
        while j < len(word2):
            result += word2[j]
            j += 1
        
        return result

        