# Problem - https://leetcode.com/problems/maximum-subarray/description/
#  Reference - https://leetcode.com/problems/maximum-subarray/solutions/1595195/cpython-7-simple-solutions-w-explanation-kb6j/

# ======= Brute Force ============

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        n = len(nums)
        def find_max_subarr(ind,s):

            if ind < 0:
                return s
            pick = find_max_subarr(ind-1,s+nums[ind],)
            not_pick = find_max_subarr(ind-1,s)
            return max(pick,not_pick)

        return find_max_subarr(n-1,0)

# Time Complexity - O(N2)
# Space Complexity - O(1)

#============= Memorization ===================

  dp = [[None]*2 for _ in range(len(nums)+1)]

  def solve(ind,must_pick):

      if ind == len(nums):
          
          dp[ind][must_pick] = 0 if must_pick else float("-inf")
          return dp[ind][must_pick]

      if dp[ind][must_pick]:
          return dp[ind][must_pick]
          
      take = nums[ind]+solve(ind+1,1)
      skip = 0 if must_pick else solve(ind+1,0)

      dp[ind][must_pick] = max(take,skip)
      return dp[ind][must_pick]

  return solve(0,0)

# Time Complexity - O(N2)
# Space Complexity - O(2*N)

#=================== Tabulation ========== 

        dp = [[0]*n for _ in range(2)]
        dp[1][0] = nums[0]
        dp[0][0] = nums[0]

        for i in range(1,n):

            dp[1][i] = max(nums[i],nums[i]+dp[1][i-1])
            dp[0][i] = max(dp[0][i-1],dp[1][i])
        
        return dp[0][n-1] 

# Time Complexity - O(N)
# Space Complexity - O(2*N)

#=============  Kadane's Algorithm =============

      curMax,maxTilNow = 0, -inf

      for ele in nums:
          curMax = max(ele,curMax+ele)
          maxTilNow = max(curMax,maxTilNow)
      return maxTilNow

# Time Complexity - O(N)
#  Space Complexity - O(1)




