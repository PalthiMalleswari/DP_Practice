#  Problem - https://leetcode.com/problems/climbing-stairs/
#  Refernce Solution - https://leetcode.com/problems/climbing-stairs/solutions/6162936/dynamic-programming-solution-by-niits-k9xe/

# ========== Pattern ===========

# n=1 -> no.of ways to climb 1 step is 1
# n=2 -> no.of ways to climb 2 steps is 2 is 1,1 or 2
# n=3 -> no.of ways to climb 3 steps is 3 is 1,1,1 or 2,1 or 1,2

so, for n=k the no.of ways to reach kth step is = no.of ways to reach k-1 + no.of ways to reach k-2

so dp[i] -> represents no.of ways to reach from 1 step to ith step 

# Recursive Relation -> dp[i] = dp[i-1]+dp[i-2]

class Solution:
  def climbStairs(self, n: int) -> int:
     
      if n in (1,2):
          return n

      prev1 = 2
      prev2 = 1

      for ele in range(3,n+1):
          cur = prev1+prev2
          prev2 = prev1
          prev1 = cur
      
      return prev1
  
Time Complexity - O(N)
Space Complexity - O(1)

# ====== Brute Force (Similar to Fibnacci Series) ==============

  def func(n):
      if n in (0,1):
        return n
      return func(n-1)+func(n-2)

Time Complexity - O(2^N)
Space Complexity - O(N) // stack space

# ========= Memorization ===========

class Solution:
    def climbStairs(self, n: int) -> int:
        
        dp = [-1]*(n+2)

        def func (k):

            if k in (0,1):
                dp[k] = k
                return dp[k]

            if dp[k] != -1:
                return dp[k]

            dp[k] = func(k-1)+func(k-2)
            return dp[k]

        return func(n+1)

Time Complexity - O(N)
Space Complexity - O(N) // stack space

# =========== Tabulation ===============

#  No Need to Store zero because it won't impact the ans, 

      dp = [0]*(n+1)
      dp[0],dp[1] = 1,1

      for i in range(2,n+1):
          dp[i] = dp[i-1]+dp[i-2]

      return dp[n]

Time Complexity - O(N)
Space Complexity - O(N) // Dp Array




