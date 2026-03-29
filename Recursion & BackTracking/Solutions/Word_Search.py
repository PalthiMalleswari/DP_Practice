#https://leetcode.com/problems/word-search/

#============ Intial Approach =================
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        n,m = len(board[0]),len(board)
        visited = [[False]*n for _ in range(m)]

        if len(word) == 1 and board[0][0]==word:
            return True
        
        def find_word(r,c,rem_word):

            if not rem_word:
                
                return True
        
            for n_r,n_c in [(r+1,c),(r-1,c),(r,c-1),(r,c+1)]:

                
                if n_r >=m or n_r<0 or n_c<0 or n_c>=n or visited[n_r][n_c] or board[n_r][n_c]!=rem_word[0]:
                    continue

                visited[n_r][n_c] = True
                
                if find_word(n_r,n_c,rem_word[1:]):
                    return True
                visited[n_r][n_c] = False
            
            return False
        
        for row in range(m):
            for col in range(n):
                if find_word(row,col,word):
                    return True
        return False

  Time Complexity -> M*N*3^L (L=Length of Word) (For Every Index there can be 4 Neighbour Choices Among them we mark visited indices, to avoid reconsidering it again, So Neary 3 unique calls)
  And the Depth of the Tree goes upto Length of the Word(L) So, find_word Time Complexity is 3^L

  Space Complexity -> L + M*N (Visited Array)

# ================= Optimized And Pruned Approach =================

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        n,m = len(board[0]),len(board)

        if len(word) == 1 and board[0][0]==word:
            return True
        
        def find_word(r,c,ind):

            if ind == len(word):
                return True

            if r >=m or r<0 or c<0 or c>=n or board[r][c]!=word[ind]:
                return False

            temp = board[r][c]
            board[r][c] = '#'
            for n_r,n_c in [(r+1,c),(r-1,c),(r,c-1),(r,c+1)]:
    
                if find_word(n_r,n_c,ind+1):
                    return True
    
            board[r][c] = temp
            
            return False
        
        for row in range(m):
            for col in range(n):
                if board[row][col]==word[0] and find_word(row,col,0):
                    return True
        return False

#=============== Most Optimal Solution ==================

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        m, n = len(board), len(board[0])

        # Pruning: character frequency check
        from collections import Counter
        board_count = Counter(sum(board, []))
        word_count = Counter(word)

        for ch in word_count:
            if word_count[ch] > board_count.get(ch, 0):
                return False

        # DFS
        def dfs(r, c, index):
            if index == len(word):
                return True

            if r < 0 or r >= m or c < 0 or c >= n or board[r][c] != word[index]:
                return False

            # mark visited
            temp = board[r][c]
            board[r][c] = '#'

            # explore 4 directions
            found = (
                dfs(r+1, c, index+1) or
                dfs(r-1, c, index+1) or
                dfs(r, c+1, index+1) or
                dfs(r, c-1, index+1)
            )

            # backtrack
            board[r][c] = temp

            return found

        # try every starting point
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:   # small pruning
                    if dfs(i, j, 0):
                        return True

        return False
            

  

            
