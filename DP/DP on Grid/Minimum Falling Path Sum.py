#Problem - https://leetcode.com/problems/minimum-falling-path-sum/description/

#============= Bottom Up Appraoch =============

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        n = len(matrix)

        dp = [[0]*n for _ in range(n)]
        for i in range(n):
            dp[0][i] = matrix[0][i]

        for i in range(1,n):
            for j in range(n):

                if j==0:
                    dp[i][j] = min(dp[i-1][j],dp[i-1][j+1])+matrix[i][j]

                elif j==n-1:
                    dp[i][j] = min(dp[i-1][j],dp[i-1][j-1])+matrix[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j],dp[i-1][j-1],dp[i-1][j+1])+matrix[i][j]
        return min(dp[n-1])

Time Complexity - O(N*N)
Space Complexity - O(N*N)

#================ Space Optimizatin Approach ============

 dp = matrix[0][:]
            
for i in range(1,n):
    
    prev_left = 0

    for j in range(n):
        
        cur_ele = dp[j]

        if j==0:
            dp[j] = min(dp[j],dp[j+1])+matrix[i][j]

        elif j==n-1:
            dp[j] = min(dp[j],prev_left)+matrix[i][j]
        else:
            dp[j] = min(dp[j],prev_left,dp[j+1])+matrix[i][j]

        prev_left = cur_ele

return min(dp)

Time Complexity - O(N*N)
Space Complexity - O(N)
