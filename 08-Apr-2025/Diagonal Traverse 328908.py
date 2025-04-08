# Problem: Diagonal Traverse - https://leetcode.com/problems/diagonal-traverse/

class Solution(object):
    def findDiagonalOrder(self, mat):
        rows = len(mat)
        cols = len(mat[0])
        res = []

        row, col = 0, 0
        direction =  -1
        for _ in range(rows*cols):
            res.append(mat[row][col])
            if direction == 1:
                if row == rows - 1:
                    col += 1
                    direction = -1
                elif col == 0:
                    row += 1
                    direction = -1
                else:
                    col -= 1
                    row += 1
            else:
                if col == cols - 1:
                    row += 1
                    direction = 1
                elif row == 0:
                    col += 1
                    direction = 1
                else:
                    col += 1
                    row -= 1
        
        return res
