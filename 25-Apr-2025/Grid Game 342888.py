# Problem: Grid Game - https://leetcode.com/problems/grid-game/

class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        prefix_mat = [[0 for _ in range(len(grid[0]) + 1)] for _ in range(2)]

        for i in range(2):
            for j in range(1, len(prefix_mat[0])):
                prefix_mat[i][j] = grid[i][j - 1] + prefix_mat[i][j - 1]
                
        min_robot_2 = float('inf')
        for j in range(1, len(prefix_mat[0])):
            robot_score = max(prefix_mat[1][j-1], (prefix_mat[0][-1] - prefix_mat[0][j]))
            min_robot_2 = min(min_robot_2, robot_score)
        
        return min_robot_2