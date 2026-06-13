# Question - https://leetcode.com/problems/coin-change-ii/description/

# Solution1
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        n = len(coins)

        dp = [[-1]*(amount+1) for _ in range(n)]
        def calculate_coins(ind,target):

            if target == 0:
                return 1
            if ind>=n:
                return 0
            if dp[ind][target] != -1:
                return dp[ind][target]

            cnt = 0
            for i in range(ind,n):
                if coins[i]<=target:
                    cnt += calculate_coins(i,target-coins[i])
            
            dp[ind][target] = cnt
            return dp[ind][target]

        return calculate_coins(0,amount)

Time Complexity - O(n*amount)+Recursive Stack Space
Space Complexity - O(n*amount)
#--------------------------------------------------------------------

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
