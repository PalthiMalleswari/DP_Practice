# Problem  -  https://leetcode.com/problems/n-queens/

# Intial Approach
# Intuition: Fill Row By Row, Collect All the invalid positions, use them to prune the invalid moves

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        not_allowed = []

        comb = [['.']*n for _ in range(n)]

        ans = []

        def possible_sol(row,col,rem_q):

            if rem_q == 0:                
                ans.append(["".join(l[:])for l in comb])
                return 

            if row >= n and col >= n:
                return
            
            for c in range(n):

                if (row,c) in not_allowed:
                    continue

                comb[row][c] = 'Q'

                for i in range(c,n):
                    not_allowed.append((row,i))

                for i in range(row,n):
                    not_allowed.append((i,c))
                
                for i in range(1,n):
                    not_allowed.append((row+i,c+i))
                
                for i in range(1,n):
                    not_allowed.append((row+i,c-i))

                possible_sol(row+1,c,rem_q-1)

                comb[row][c] = '.'

                for i in range(c,n):
                    not_allowed.remove((row,i))

                for i in range(row,n):
                    not_allowed.remove((i,c))
                
                for i in range(1,n):
                    not_allowed.remove((row+i,c+i))

                for i in range(1,n):
                    not_allowed.remove((row+i,c-i))

        possible_sol(0,0,n)

        return ans



Time Complexity - O(N!)
Space Complexity - O(N) // Not allowed List

# ================= Optimal Solution ==================
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        

        comb = [['.']*n for _ in range(n)]

        ans = []

        def possible_sol(row):

            if row == n:
                ans.append(["".join(l) for l in comb])
                return 
            
            for c in range(n):

                if isSafe(row,c):
                    print(comb)
                    comb[row][c] = 'Q'
                    possible_sol(row+1)
                    comb[row][c] = '.'

        def isSafe(r,c):

            for i in range(r):
                if comb[i][c]=='Q':
                    return False
            

            for i in range(1,n):
                if r-i>=0 and c-i>=0 and comb[r-i][c-i]=='Q':
                    return False

            for i in range(1,n):
                if r-i>=0 and c+i<n and comb[r-i][c+i]=='Q':
                    return False

          # ======== Other Way to check back diagonals ======= 
          # for i in range(1,min(r,c)+1):
            #     if comb[r-i][c-i]=='Q':
            #         return False
          
            # for i in range(1,min(r,n-c-1)+1):
            #     if comb[r-i][c+i]=='Q':
            #         return False
            return True

        possible_sol(0)
        return ans

Time Complexity - O(N!)
Space Complexity - O(1)
