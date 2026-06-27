#Problem - https://leetcode.com/problems/maximal-square/description/

dp[i][j] = Denotes Maximum Square side ending at index i,j
dp[i][j] = min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1])+1 


#========== 2D Bottom up Approach =================
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n,m = len(matrix),len(matrix[0])

        dp = [[0]*m for _ in range(n)]
        ans = 0
        for i in range(n):
            for j in range(m):
                
                if matrix[i][j] == '1':
                    if i==0 or j ==0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1

                    ans = max(ans,dp[i][j])
        
        return ans*ans

Time Complexity - O(M*N)
Space Complexity - O(M*N)

We Optimize the space because current state only depends on previous row, and current row we don't have to store all previous rows
