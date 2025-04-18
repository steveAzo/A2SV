# Problem: Find Common Characters - https://leetcode.com/problems/find-common-characters/

class Solution(object):
    def commonChars(self, words):
        result = []
        common = Counter(words[0])
        for word in words[1:]:
            common &= Counter(word)
        
        for char, freq in common.items():
            result.extend([char]*freq)
            
        return result
        