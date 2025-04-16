# Problem: Longest Nice Substring - https://leetcode.com/problems/longest-nice-substring/

class Solution(object):
    def isNice(self, subs):
        for i in range(len(subs)):
            otherCase = chr(ord('a') + (ord(subs[i]) - ord('A'))) if ord(subs[i]) < ord('a') else chr(ord('A') + (ord(subs[i]) - ord('a')))
            if otherCase not in subs:
                return False
        return True

    def longestNiceSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        nice_res = ''
        for i in range(len(s) - 1):
            for j in range(i+1, len(s)):
                if self.isNice(s[i:j+1]):
                    if (j-i+1) > len(nice_res):
                        nice_res = s[i:j+1]
        
        return nice_res


        