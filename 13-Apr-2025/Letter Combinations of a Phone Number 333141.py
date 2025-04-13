# Problem: Letter Combinations of a Phone Number - https://leetcode.com/problems/letter-combinations-of-a-phone-number/

import itertools

class Solution(object):
    def letterCombinations(self, digits):
        if not digits:
            return []
            
        dig_map = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }

        n = len(digits)
        dgts = list(map(int, digits))

        res = []
        for dgt in dgts:
            res.append(dig_map[dgt])
        
        result = [''.join(combination) for combination in itertools.product(*res)]

        return [strs for strs in result if len(strs) == n]