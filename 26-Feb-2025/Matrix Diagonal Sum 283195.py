# Problem: Matrix Diagonal Sum - https://leetcode.com/problems/matrix-diagonal-sum/description/

class Solution(object):
    def diagonalSum(self, mat):
        n = len(mat)

        sum_diagonals = 0
        for i in range(n):
            sum_diagonals += mat[i][i]
            sum_diagonals += mat[i][n - i - 1]

        if n % 2 == 1:
            sum_diagonals -= mat[n//2][n//2]
        return sum_diagonals
        