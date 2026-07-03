#Problem - https://leetcode.com/problems/unique-paths/description/

#================ Recursive Approach =========


 dp = [[-1]*n for i in range(m)]

        def get_paths(i,j):

            
            if i == m-1 and j == n-1:
                return 1
            
            if dp[i][j] != -1:


                return dp[i][j]

            # right
            right,down = 0, 0
            if j<n-1:

                right = get_paths(i,j+1)
            if i< m-1:
                down = get_paths(i+1,j)

            dp[i][j] = right+down
            
            return dp[i][j]
        
        return get_paths(0,0)

Time Complexity - O(m*n)
Space Complexity - O(m*n) +stack space

#================ Bottom Up Approach ================

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        dp = [[0]*n for _ in range(m)]

        for j in range(n):
            dp[0][j] = 1
        
        for i in range(m):
            dp[i][0] = 1
        
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j]+dp[i][j-1]
        return dp[m-1][n-1]

  Time Complexity - O(m*n)
Space Complexity - O(m*n) 

#================ Optimal Approach ================

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        dp = [ 1 for _ in range(n)]
                
        for i in range(1,m):
            for j in range(1,n):
                dp[j] = dp[j]+dp[j-1]

        return dp[n-1]

  Time Complexity - O(M*N)
Space Complexity - O(N)
