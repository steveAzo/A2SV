# Problem: Toeplitz matrix - https://leetcode.com/problems/toeplitz-matrix/description/

class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrixrix: List[List[int]]
        :rtype: bool
        """
        n, m = len(matrix), len(matrix[0])
        for i in range(n - 1):
            for j in range(m - 1):
                if matrix[i][j] != matrix[i+1][j+1]:
                    return False
        return True
            