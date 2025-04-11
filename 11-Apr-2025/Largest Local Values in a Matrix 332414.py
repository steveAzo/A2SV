# Problem: Largest Local Values in a Matrix - https://leetcode.com/problems/largest-local-values-in-a-matrix/

class Solution(object):
    def largestLocal(self, grid):
        result = []

        n = len(grid)
        m = len(grid[0])
        for i in range(1, n-1):
            res = []
            for j in range(1, n-1):
                res.append(max(grid[i][j], grid[i-1][j-1], grid[i-1][j]
                           ,grid[i-1][j+1], grid[i][j-1], grid[i][j+1]
                           ,grid[i+1][j-1], grid[i+1][j], grid[i+1][j+1] 
                        ))
            result.append(res)
        
        return result
        