# Problem: Search a 2D Matrix - https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1

        while left < right:
            mid = (left + right) // 2
            row = mid // m
            col = mid % m
            if matrix[row][col] >= target:
                right = mid
            else:
                left = mid + 1
        
        row = left // m
        col = left % m
        print(matrix[row][col])
        return matrix[row][col] == target