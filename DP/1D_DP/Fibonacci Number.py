#  Problem - https://leetcode.com/problems/fibonacci-number/description/

class Solution:
    def fib(self, n: int) -> int:

        dp = {}
        
        def get_fib(ind):

            if ind in (0,1):
                dp[ind] = ind
                return dp[ind]
            if ind in dp:
                return dp[ind]

            dp[ind] = get_fib(ind-1)+get_fib(ind-2)

            return dp[ind]

        return get_fib(n)

Time Complexity - O(N)
Space Complexity - O(N+N) // Stack Space 


# =============== Memoriation ===============

class Solution:
    def fib(self, n: int) -> int:

        if n <= 1:
            return n
            
        dp = [0]*(n+1)

        dp[0],dp[1] = 0,1

        for i in range(2,n+1):

            dp[i] = dp[i-1]+dp[i-2]
        
        return dp[n]

Time Complexity - O(N)
Space Complexity - O(N)

# ================= Space Optimization ===============

class Solution:
    def fib(self, n: int) -> int:

        if n <= 1:
            return n

        prev2,prev1 = 0,1

        for i in range(2,n+1):

            cur = prev1+prev2
            prev2 = prev1
            prev1 = cur
        
        return prev1

Time Complexity - O(N)
Space Complexity - O(1)


      
