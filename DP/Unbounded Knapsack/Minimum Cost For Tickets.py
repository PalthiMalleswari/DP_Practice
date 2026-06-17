# Problem - https://leetcode.com/problems/minimum-cost-for-tickets/

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        n = len(days)
        memo = {}

        def dfs(i):

            if i >= n:
                return 0

            if i in memo:
                return memo[i]

            # 1-day pass
            j = i
            while j < n and days[j] < days[i] + 1:
                j += 1

            one = costs[0] + dfs(j)

            # 7-day pass
            j = i
            while j < n and days[j] < days[i] + 7:
                j += 1

            seven = costs[1] + dfs(j)

            # 30-day pass
            j = i
            while j < n and days[j] < days[i] + 30:
                j += 1

            thirty = costs[2] + dfs(j)

            memo[i] = min(one, seven, thirty)

            return memo[i]

        return dfs(0)

Time Complexity - O(3*N) Nearly N
Space Compelxity - O(N)

#==================== Other Approach =========
 dp = [0]*366

for i in range(1,366):
    if i not in days:
        dp[i] = dp[i-1]
    else:
        dp[i] = min(dp[i-1]+costs[0],dp[max(0,i-7)]+costs[1],dp[max(0,i-30)]+costs[2])

return dp[365]

Time Complexity - O(366)
Space Complexity - O(366)
