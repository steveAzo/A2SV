# Problem: Excel Sheet Column Title - https://leetcode.com/problems/excel-sheet-column-title/description/?envType=problem-list-v2&envId=string

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []

        while columnNumber > 0:
            columnNumber -= 1
            char = chr(ord('A') + columnNumber % 26)
            res.append(char)
            columnNumber = columnNumber// 26
        
        return ''.join(reversed(res))
