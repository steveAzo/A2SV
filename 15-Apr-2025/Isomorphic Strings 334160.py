# Problem: Isomorphic Strings - https://leetcode.com/problems/isomorphic-strings/

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        seen_s = [0]*256
        seen_t = [0]*256

        for i, (a, b) in enumerate(zip(s, t), 1):
            a = ord(a)
            b = ord(b)

            if seen_s[a] != seen_t[b]:
                return False
            seen_s[a] = seen_t[b] = i
        
        return True
        