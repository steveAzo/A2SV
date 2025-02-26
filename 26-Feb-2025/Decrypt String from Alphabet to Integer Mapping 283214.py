# Problem: Decrypt String from Alphabet to Integer Mapping - https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/description/

from string import ascii_lowercase as alp

class Solution(object):
    def freqAlphabets(self, s):
        hash_map = {}

        i = 1
        for char in alp:
            hash_map[i] = char
            i += 1
        
        result = ''
        j = 0
        while j < len(s):
            if j + 2 < len(s) and s[j + 2] == '#':
                num = int(s[j])*10 + int(s[j + 1])
                result += hash_map[num]
                j = j + 3
            else:
                result += hash_map[int(s[j])]
                j += 1

        return result


        