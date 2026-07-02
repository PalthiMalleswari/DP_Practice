#https://leetcode.com/problems/maximum-number-of-points-with-cost/description/

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
        n,m = len(points),len(points[0])

        dp = [[0]*m for _ in range(n)]
        
        ans = 0
        for j in range(m):
            dp[0][j] = points[0][j]
            ans = max(ans,dp[0][j])
        
       
        for i in range(1,n):
            for j in range(m):
                for k in range(m):

                    dp[i][j] = max(dp[i][j],dp[i-1][k]-abs(j-k))
                
                dp[i][j] += points[i][j]                
                ans = max(dp[i][j],ans)
        return ans 
      
#===================== Optimized Solution (Didn't get the Intuition for Left,Right ?) =======================
        rows = len(points)
        cols = len(points[0])

       
        prev = points[0][:]

       
        for i in range(1, rows):

            left = [0] * cols
            right = [0] * cols


            left[0] = prev[0]

            for j in range(1, cols):

                left[j] = max(left[j - 1] - 1, prev[j])


            right[cols - 1] = prev[cols - 1]

            for j in range(cols - 2, -1, -1):
                right[j] = max(right[j + 1] - 1, prev[j])

            curr = [0] * cols

            for j in range(cols):
                curr[j] = points[i][j] + max(left[j], right[j])

            prev = curr

        return max(prev)

Time Complexity - O(N*M)
Space Complexity - O(N*(M+M))

        
