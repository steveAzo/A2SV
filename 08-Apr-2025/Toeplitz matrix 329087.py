# Problem: Toeplitz matrix - https://leetcode.com/problems/toeplitz-matrix/description/

class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrixrix: List[List[int]]
        :rtype: bool
        """
        n, m = len(matrix), len(matrix[0])
        res = []

        for col in range(1,len(matrix[0])):
            row = 1
            i = 1
            while row < len(matrix) and col < len(matrix[0]):
                if matrix[row][col] != matrix[row-1][col-1]:
                    return False
                row += 1
        
        for row in range(1,len(matrix)):
            col = 1
            i = 1

            while row < len(matrix) and col < len(matrix[0]):
                if matrix[row][col] != matrix[row-1][col-1]:
                    return False
                col +=1

        return True
            