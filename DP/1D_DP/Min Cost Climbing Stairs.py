# Problem - https://algomaster.io/learn/dsa/min-cost-climbing-stairs


# =============== Memorization =================
        memo = {}
        def min_cost(ind):
            if ind<0:
                return 0
            if ind in memo:
                return memo[ind]

            t = min(min_cost(ind-1),min_cost(ind-2))
            if ind < n:
                t = t + cost[ind]
            memo[ind] = t
            return t
        n = len(cost)
        return min_cost(n)
Time Complexity - O(N)
Space Complexity - O(N)

# ============== Most Efficient Way ===================

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        prev2,prev1 = 0,0
        for i in range(2,n+1):
            t = min(cost[i-1]+prev1,cost[i-2]+prev2)
            prev2 = prev1
            prev1 = t
        return prev1
Time Complexity - O(N)
Space Complexity - O(1)


       
