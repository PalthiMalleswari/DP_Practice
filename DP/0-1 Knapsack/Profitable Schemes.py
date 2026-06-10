# Problem - https://leetcode.com/problems/profitable-schemes/description/

#Recursive Version with (MLE for test case 40/45)
# State Exploision due to profit state
# we should keep min(minProfit,prf+profit[i]) we need minProfit

class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        
        nn = len(group)
        dp = {}

        def no_of_ways(ind,prf,rem_n):

            if ind==-1:
                if prf<minProfit:
                    return 0
                else:
                    return 1

            if (ind,prf,rem_n) in dp:
                return dp[(ind,prf,rem_n)]

            dont = no_of_ways(ind-1,prf,rem_n)
            take = 0
            if rem_n>=group[ind]:
                take = no_of_ways(ind-1,prf+profit[ind],rem_n-group[ind])
            dp[(ind,prf,rem_n)] = dont+take
            return dp[(ind,prf,rem_n)]

        return no_of_ways(nn-1,0,n)
      
  Time Complexity - O(len(profits)*sum(profit)*n)
  Space Complexity - O(len(profits)*sum(profit)*n)

#================ Top Down Approach (With State Optimizations) =============

    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        
        nn = len(group)
        dp = {}
        Mod = 10**9+7

        def no_of_ways(ind,prf,rem_n):

            if ind>=nn:
                if prf<minProfit:
                    return 0
                else:
                    return 1

            if (ind,prf,rem_n) in dp:
                return dp[(ind,prf,rem_n)]

            dont = no_of_ways(ind+1,prf,rem_n)
            take = 0
            if rem_n+group[ind]<=n:
                take = no_of_ways(ind+1,min(minProfit,prf+profit[ind]),rem_n+group[ind])
            dp[(ind,prf,rem_n)] = (dont+take)%Mod
            return dp[(ind,prf,rem_n)]

        return no_of_ways(0,0,0)
        
Time Complexity - O(len(profits)*minProfit*n)
Space Complexity - O(len(profits)*minProfit*n) + Recursive Stack Space

#================ Bottom Up Approach =============

dp = [[[0]*(n+1)for _ in range(minProfit+1)] for _ in range(nn+1)]
dp[0][0][0] = 1

for i in range(nn):
    gp = group[i]
    prf = profit[i]
    for pf in range(minProfit+1):
        for rem in range(n+1):
            new_prf = min(minProfit,pf+prf)

            dp[i+1][pf][rem] += dp[i][pf][rem]
            
            if rem+gp<=n:
                dp[i+1][new_prf][rem+gp] += dp[i][pf][rem]

return sum(dp[nn][minProfit])%Mod

Time Complexity - O(len(profits)*minProfit*n)
Space Complexity - O(len(profits)*minProfit*n)

#============== Space Optimization (By Avoiding Overflows) =============

        dp = [[0]*(n+1)for _ in range(minProfit+1)]

        dp[0][0] = 1

        for gp,prf in zip(group,profit):
 
            for pf in range(minProfit,-1,-1):
                for rem in range(n-gp,-1,-1):
                    new_prf = min(minProfit,pf+prf)

                    dp[new_prf][rem+gp] =(dp[new_prf][rem+gp]+dp[pf][rem])%Mod
        
        return sum(dp[minProfit])%Mod

Time Compexity - O(len(profit)*minProfit*n)
Space Complexity - O(minProfit*n)
