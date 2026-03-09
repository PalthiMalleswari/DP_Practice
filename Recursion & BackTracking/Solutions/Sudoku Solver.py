# Problem - https://leetcode.com/problems/sudoku-solver/description/

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def is_valid(r,c,ch):

            startRow,startCol = r//3*3,c//3*3

            for i in range(9):
                if board[r][i] == ch or board[i][c] == ch or board[startRow+i//3][startCol+i%3] == ch:
                    return False
            return True

        
        def solve(r, c):

            if r == 9:
                return True

            if c == 9:
                return solve(r+1,0)

            if board[r][c] != '.':
                return solve(r,c+1)

            for num in '123456789':
                if is_valid(r,c,num):

                    board[r][c] = num

                    if solve(r,c+1):
                        return True

                    board[r][c] = '.'

            return False 

        return solve(0,0)

Time Complexity -> Branching Factor = 9 (Each Empty cell have 1-9 possible values) depth = no.of empty cells = m and is_valid = N (Scans all rows,cols,box)
Total Complexity -> O(9*n)^m

Space Complexity -> O(m) recursive stack space (Excluding Ans Storage)

# =========================== Memorization the Is_Valid =======================

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows_map = [set() for _ in range(9)]
        col_map = [set() for _ in range(9)]
        box_map = [set() for _ in range(9)]
        
        def solve(r, c):

            if r == 9:
                return True

            if c == 9:
                return solve(r+1,0)

            if board[r][c] != '.':
                return solve(r,c+1)

            for num in '123456789':

                box_num = r//3*3+c//3
                if num in rows_map[r] or num in col_map[c] or num in box_map[box_num]:
                    continue
                
                board[r][c] = num

                rows_map[r].add(num)
                col_map[c].add(num)
                box_map[box_num].add(num)

                if solve(r,c+1):
                    return True

                board[r][c] = '.'

                rows_map[r].remove(num)
                col_map[c].remove(num)
                box_map[box_num].remove(num)

            return False 
          
      # Store Already Filled Elements 
        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    num = board[r][c]
                    rows_map[r].add(num)
                    col_map[c].add(num)
                    box_map[(r//3)*3 + c//3].add(num)

        return solve(0,0)

Time Complexity ->   Branching Factor = 9 (Each Empty cell have 1-9 possible values) depth = no.of empty cells = m and is_valid = O(1)
Total Complexity -> O(9^m)

Space Complexity -> O(m)+O(9^6)
