# Problem: Set Matrix Zeroes - https://leetcode.com/problems/set-matrix-zeroes/

class Solution(object):
    def setZeroes(self, matrix):
        n = len(matrix)
        m = len(matrix[0])

        rows = [True]* n
        cols = [True]* m

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    rows[i] = False
                    cols[j] = False
        
        for i in range(n):
            for j in range(m):
                if rows[i] == False or cols[j] == False:
                    matrix[i][j] = 0
            
            
        