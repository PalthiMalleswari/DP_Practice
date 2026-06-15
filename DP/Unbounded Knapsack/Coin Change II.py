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

#=================== 2D Memorization ==========================

        n = len(coins)

        dp = [[0]*(amount+1) for _ in range(n+1)]

        for i in range(n+1):
            dp[i][0] = 1

        for i in range(1,n+1):

            for amt in range(amount+1):
                dp[i][amt] = dp[i-1][amt]
                if amt >= coins[i-1]:
                    dp[i][amt] += dp[i][amt-coins[i-1]]

        return dp[n][amount]
        
Time Complexity - O(n*amount)
Space Complexity - O(n*amount)

#=================  Space Optimization ================
        n = len(coins)

        dp = [0]*(amount+1)

        dp[0] = 1
        for i in range(1,n+1):
            temp = [0]*(amount+1)
            for amt in range(amount+1):
                temp[amt] = dp[amt]
                if amt >= coins[i-1]:
                    temp[amt] += temp[amt-coins[i-1]]
            dp=temp

        return dp[amount]

Time Complexity - O(n*amount)
Space Complexity - O(n*amount) for each coin, we're taking temp array 

#=================== Most Optimal Approach ===============

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        n = len(coins)
        dp = [0]*(amount+1)

        dp[0] = 1
        for coin in coins:
            for amt in range(coin,amount+1):                
                dp[amt] += dp[amt-coin]
        return dp[amount]

Time Complexity - O(N*amount)
Space Complexity - O(N)
