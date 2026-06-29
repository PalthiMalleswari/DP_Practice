#PRoblem - https://leetcode.com/problems/minimum-path-sum/description/

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n,m = len(grid),len(grid[0])

        dp = [0]*m
        dp[0] = grid[0][0]
        for j in range(1,m):
            dp[j] = dp[j-1]+grid[0][j]
        
        for i in range(1,n):
            dp[0]+=grid[i][0]

            for j in range(1,m):
                
                dp[j] = grid[i][j] + min(dp[j-1],dp[j])
                
        return dp[m-1]


Time Complexity - O(M*N)
Space Complexity - O(N)
