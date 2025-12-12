# Question - https://leetcode.com/problems/coin-change-ii/description/

# Solution

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        n = len(coins)

        dp = [ [-1 for _ in range(amount+1)] for _ in range(n)]
        
        def calculate_coins(ind,target):

            if ind == 0:

                dp[ind][target] = 1 if (target%coins[0])==0 else 0
                
                return dp[ind][target]

            if dp[ind][target] != -1:

                return dp[ind][target]

            not_take = calculate_coins(ind-1,target)
            
            take = 0
            if coins[ind] <= target:

                take = calculate_coins(ind,target-coins[ind])
            
            dp[ind][target] = take+not_take
            
            return dp[ind][target]
        
        
        calculate_coins(n-1,amount)

        return dp[n-1][amount]

## Time Complexity  - O(amount*len(Coins))
##  Space Complexity - O(amount*n)  For dp array 
