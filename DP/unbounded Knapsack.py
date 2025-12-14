# Question - https://takeuforward.org/plus/dsa/problems/unbounded-knapsack

# Memorization

class Solution:
    def unboundedKnapsack(self, wt, val, n, W):

        #  dp[ind][weight] represents for weight,the maximum value you get from o to ind
        dp = [ -1 for _ in range(wt+1) for _ in range(n+1)]

        def calculate_max_value(ind,weight):

            if ind == 0:
                
                dp[ind][weight] = (weight/wt[ind])*val[ind]
                return dp[ind][weight]

            if dp[ind][weight] != -1:

                return dp[ind][weight]

            # not take
            not_take = calculate_max_value(ind-1,weight)

            take = 0

            if wt[ind] <= weight:
                # take
                take = calculate_max_value(ind,weight-wt[ind]) + val[ind]
            
            dp[ind][weight] = max(take,not_take)

            return dp[ind][weight]

# Time Complexity - O(N*Weight) total N*Weight states in dp array
# Space Complexity - O(N*Weight) + O(N) for stach space

#  Tabulation

dp = [ 0 for _ in range(wt+1) for _ in range(n+1)]

n = len(values)

for w in range(wt):

    dp[0][w] = w//wt[0] * val[0]
    
for ind in range(1,n):

    for w in range(wt+1):

        not_take = dp[ind-1][w]

        take = 0

        if wt[ind] <= w:

            take = dp[ind][w-wt[ind]] + val[ind]
        
        dp[ind][w] = max(take,not_take)
  
return dp[n-1][wt]

# Time Complexity - O(N*Weight) total N*Weight states in dp array
# Space Complexity - O(N*Weight) + O(N) for stach space

# Space Optimization

# Look For Prev Preservation logic here https://takeuforward.org/data-structure/unbounded-knapsack-dp-23
#  We don't need entire previoud array here we only need corresponding index value and other value in the current row 
# So we'll store the previous value in the current row before hand, and later update it to maximum value

cur = [0 for i in range(wt+1)]

for w in range(wt):

    cur[w] = w//wt[0] * val[0]

for ind in range(1,n):

    
    for w in range(wt+1):

        not_take = cur[w]

        take = 0

        if wt[ind] <= w:

            take = cur[w-wt[ind]]+val[ind]
        
        cur[w] = max(take,not_take)

return cur[wt]

