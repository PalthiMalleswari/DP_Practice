#Problem - https://leetcode.com/problems/count-square-submatrices-with-all-ones/description/

#========== Bottom Up Approach ==================

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        
        m = len(matrix)
        n = len(matrix[0])

        dp = [[0]*n for _ in range(m)]
        ans = 0
        
        for i in range(m):
            for j in range(n):

                if matrix[i][j] == 1:
                   
                    if i==0 or j==0:
                        dp[i][j] = 1
                    
                    else:
                        dp[i][j] = min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1])+1
                    
                    ans += dp[i][j]
        return ans

Time Complexity - O(N*M)
Space Complexity - O(M*N)

We can optimize the space too, as current row/state is depending on previous row and curretn row
