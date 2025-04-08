# Problem: Set Matrix Zeroes - https://leetcode.com/problems/set-matrix-zeroes/

class Solution(object):
    def setZeroes(self, matrix):
        zero_indices = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zero_indices.append([i, j])
        
        for index in zero_indices:
            for k in range(len(matrix[0])):
                matrix[index[0]][k] = 0
            
            for l in range(len(matrix)):
                matrix[l][index[1]] = 0
            
        