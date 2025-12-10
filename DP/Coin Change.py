# Question - https://leetcode.com/problems/coin-change/description/


## Naive Approach
        def calculate_no_of_coins(target):

            if target == 0:

                return 0

            min_count = float('inf')

            for coin in coins:
                
                if coin > target:

                    continue

                count = calculate_no_of_coins(target-coin)

                if count >= 0 and count< min_count:
                    
                    min_count = 1 + count

            return -1 if (min_count == float("inf")) else min_count
            
            return calculate_no_of_coins(amount)
##  Time Complexity

"""

Exponential — specifically:
O(c^amount)

where:

c = number of coin denominations

amount = target

Why?

For each call to calculate_no_of_coins(target):

  > It iterates through all coins

  > For each coin, it recursively calls the function again with a smaller target

This produces a recursion tree where:

  > Each level has up to c branches

  > Depth can go up to amount

So total worst-case combinations =
c * c * c * ... (amount times) = c^amount

"""
## Space Complexity - O(amount)

## Memorization

        # Denotes min no.of coins needed to make this amount = i
        dp = [ float("inf") for _ in range(amount+1)] 


        def calculate_no_of_coins(target):

            if target == 0:

                dp[0] = 0

                return dp[0]

            if dp[target] != float('inf'):

                return dp[target]

            min_count = float('inf')

            for coin in coins:
                
                if coin > target:

                    continue

                count = calculate_no_of_coins(target-coin)

                if count >= 0 and count< min_count:
                    
                    min_count = 1 + count

            dp[target] = -1 if (min_count == float("inf")) else min_count
            
            return dp[target]

        calculate_no_of_coins(amount)

        return dp[amount]

"""
Time Complexity - O(amount × c)

where:

amount = target value

c = number of coin denominations

Why?

Memoization ensures each subproblem (target) from 1 → amount is computed only once.

Inside each computation:

You loop through all c coins

So total work:

amount subproblems × c iterations each
→ O(amount × c)

Space Complexity - O(amount)

"""


#### Tabulation  version 1

        dp = [ float("inf") for _ in range(amount+1)] 

        dp[0] = 0

        for i in range(1,amount+1):

            min_count = float("inf")

            for coin in coins:

                if coin > i:

                    continue

                count = dp[i-coin]

                if count >=0 and count<min_count:
                    
                    min_count = 1 + count

            dp[i] = -1 if (min_count == float("inf")) else min_count
        
        return dp[amount]

#### Tabulation  version 2


        dp = [ float("inf") for _ in range(amount+1)] 

        dp[0] = 0

        for i in range(1,amount+1):

            for coin in coins:
                
                if i >= coin:
        
                    dp[i] = min(dp[i],1+dp[i-coin])

        return dp[amount] if dp[amount] != float("inf") else -1

# Time Complexity - O(amount × c)
# Space Complexity - O(amount) for dp array


