#Problem - https://leetcode.com/problems/out-of-boundary-paths/description/



#================== Straight Forward Solution =======================

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        
        grid = [[0]*n for _ in range(m)]
        memo = {}
        Mod = 10**9+7
        def count_boundary_paths(i,j,moves):
            if i<0 or i>=m or j<0 or j>=n:
                return 1
            if moves <=0:
                return 0
            if (i,j,moves) in memo:
                return memo[(i,j,moves)]

            left = count_boundary_paths(i,j-1,moves-1)
            right = count_boundary_paths(i,j+1,moves-1)
            dwn = count_boundary_paths(i-1,j,moves-1)
            up = count_boundary_paths(i+1,j,moves-1)
            memo[(i,j,moves)] = (left+right+dwn+up)%Mod
            return memo[(i,j,moves)]

        return count_boundary_paths(startRow,startColumn,maxMove)
  Time Complexity - O(M*N*max_moves)

  Space Complexity - O(M*N*max_moves) + Stack Space 

#======================= Intial Approach I Tried =====================
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        
        grid = [[0]*n for _ in range(m)]
        summ = [[0]*n for _ in range(m)]
        Mod = 10**9 + 7
        if maxMove == 0:
            return 0

        for i in range(m):
            for j in range(n):
                
                for ni,nj in [(-1,0),(0,1),(0,-1),(1,0)]:

                    if i+ni<0 or i+ni>=m or j+nj<0 or j+nj>=n:
                        
                        grid[i][j]+=1
                summ[i][j] = grid[i][j]        

        for moves in range(maxMove-1):

            temp_grid =[[0]*n for _ in range(m)]
            

            for i in range(m):

                for j in range(n):

                    if j+1<n:
                        temp_grid[i][j]+= grid[i][j+1]
                    if i+1<m:
                        temp_grid[i][j]+=grid[i+1][j]
                    if i-1>=0:
                        temp_grid[i][j] += grid[i-1][j]
                    if j-1>=0:
                        temp_grid[i][j] += grid[i][j-1]

                    temp_grid[i][j] %= Mod
                    summ[i][j] += (temp_grid[i][j]%Mod)
                    summ[i][j] %= Mod
            
            grid = temp_grid
    
        return summ[startRow][startColumn]

      Time Complexity - O(Moves*M*N)
      Space Complexity - O((M*N)+(M*N)) one for grid other for sum
