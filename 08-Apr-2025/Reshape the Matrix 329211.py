# Problem: Reshape the Matrix - https://leetcode.com/problems/reshape-the-matrix/

class Solution(object):
    def matrixReshape(self, mat, r, c):
        if len(mat)*len(mat[0]) != r*c:
            return mat

        x, y = 0, 0
        new_matrix = [[0 for _ in range(c)] for _ in range(r)]
        for i in range(r):
            for j in range(c):
                new_matrix[i][j] = mat[x][y]
                if y + 1 >= len(mat[0]):
                    y = 0
                    x += 1
                else:
                    y += 1
        
        return new_matrix



        