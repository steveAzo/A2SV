# Problem: Decrypt String from Alphabet to Integer Mapping - https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/description/

class Solution(object):
    def freqAlphabets(self, s):
        result = ''
        j = 0

        while j < len(s):
            if j + 2 < len(s) and s[j + 2] == '#':
                num = int(s[j])*10 + int(s[j + 1])
                result += chr(96 + num)
                j = j + 3
            else:
                result += chr(96 + int(s[j]))
                j += 1

        return result