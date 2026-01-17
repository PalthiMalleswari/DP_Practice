#  Problem - https://leetcode.com/problems/house-robber/description/
#  Dp[i] = Denotes max amount we can rob at index i form 0
#  1D DP Pattern -

"""
-> 1D DP – “Decision at each index”
  Pattern idea:
    At index i, you decide:
      - take something
      - don’t take something
    Your choice depends on previous states.
  
dp[i] = min / max / count of: dp[i-1], dp[i-2], ...
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)

        dp = [-1]*n

        def rob_hs(ind):

            if ind < 0:
                return 0
            
            if dp[ind] != -1:

                return dp[ind]

            # Pick 
            pick = rob_hs(ind-2)+nums[ind]
            
            # Not Pick
            not_pick = rob_hs(ind-1)

            dp[ind] = max(pick,not_pick)

            return dp[ind]
        
        rob_hs(n-1)
        return dp[n-1]

  #  Time Complexity - O(N)
  #  Space complexity - O(N+N) (For Stack and Dp Array)

# =============== Tabulation ================

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)
        if n == 1:
            return nums[0]

        dp = [-1]*n
        
        dp[0] = nums[0]
        dp[1] = max(nums[1],nums[0])

        for i in range(2,n):
            dp[i] = max(dp[i-2]+nums[i],dp[i-1])
        
        return dp[n-1]

#  Time Complexity - O(N)
#  Space Complexity - O(N)

# ============ Space Optimization =================== 

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)
        if n == 1:
            return nums[0]
        
        prev2 = nums[0]
        prev1 = max(nums[1],nums[0])

        for i in range(2,n):
            cur = max(prev2+nums[i],prev1)

            prev2 = prev1
            prev1 = cur
        
        return prev1

#  Time Complexity - O(N)
#  Space Complexity - O(1)

