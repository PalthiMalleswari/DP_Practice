#Problem - https://algomaster.io/learn/dsa/paint-house


#================= Top Down Memorization ==========
#State -  minimum cost to paint houses at index ind with previous painted color as prev_color  

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        m = 3
        memo = {}

        def min_cost(ind,prev_ind):
            if ind >= n:
                return 0
            if (ind,prev_ind) in memo:
                return memo[(ind,prev_ind)]

            ans = float('inf')
            for i in range(3):
                if i != prev_ind:
                    ans = min(ans,min_cost(ind+1,i)+costs[ind][i])
            memo[(ind,prev_ind)] = ans
            return ans
        return min_cost(0,-1)


Time Complexity - O(N*3)
Space Complexity - O(N*3) + stack space

#============ Bottom Up Approach ====================

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        m = 3
        dp = [[0]*3 for _ in range(n)]
        
        for j in range(3):
            dp[0][j] = costs[0][j]

        for i in range(1,n):
            for j in range(3):
                if j==0:
                    dp[i][j] = min(dp[i-1][1],dp[i-1][2])
                elif j==1:
                    dp[i][j] = min(dp[i-1][0],dp[i-1][2])
                else:
                    dp[i][j] = min(dp[i-1][0],dp[i-1][1])

                dp[i][j] += costs[i][j]

        return min(dp[n-1])

Time Complexity - O(N*3)
Space Complexity - O(N*3)

#============= Bottom up Optimized Approach ===========

#State - Minimum Cost to paint House at Index - ind with color j

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        m = 3
        dp = costs[0][:]

        for i in range(1,n):
            prev0,prev1,prev2 = dp[0],dp[1],dp[2]

            dp[0] = min(prev1,prev2) + costs[i][0]
        
            dp[1] = min(prev0,prev2)+costs[i][1]
        
            dp[2] = min(prev0,prev1) + costs[i][2]

        return min(dp)

Time Complexity - O(N)
Space Complexity - O(N)

