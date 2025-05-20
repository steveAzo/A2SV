# Problem: Pascal's Triangle II - LeetCode - https://leetcode.com/problems/pascals-triangle-ii/

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = []
        def printIth(row, col):
            ans = 1
            for i in range(col):
                ans *= (row - i)
                ans = ans// (i + 1)
            
            return ans
        
        for i in range(rowIndex + 1):
            res.append(printIth(rowIndex, i))

        return res