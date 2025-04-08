# Problem: Valid Sudoku - https://leetcode.com/problems/valid-sudoku/

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for row in range(9):
            seen = set()
            for col in range(9):
                if board[row][col] != '.':
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        
        for col in range(9):
            seen = set()
            for row in range(9):
                if board[row][col] != '.':
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])

        # check for 3 x 3 grid
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                seen = set()
                for row in range(box_row, box_row + 3):
                    for col in range(box_col, box_col + 3):
                        if board[row][col] != '.':
                            if board[row][col] in seen:
                                return False
                            seen.add(board[row][col])
        
        return True