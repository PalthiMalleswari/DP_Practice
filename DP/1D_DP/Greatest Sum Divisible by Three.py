# Problem - https://leetcode.com/problems/greatest-sum-divisible-by-three/description/
# Brute Force - Keep State as ind,sum  mmeory limit exceed

#Memorization

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}
        def max_sum(ind,rem):

            if ind >= n:
                if rem == 0:
                    return 0
                return float('-inf')
            if (ind,rem) in memo:
                return memo[(ind,rem)]

            pick = max_sum(ind+1,(rem+nums[ind])%3)+nums[ind]
            not_pick = max_sum(ind+1,rem)

            memo[ind] = max(pick,not_pick)
            return memo[ind]
      return max_sum(0,0)

Time Complexity - 3*n
Space Complexity - O(N*3)

# Bottom Up Approach

  dp = [0, float('-inf'), float('-inf')]

  for num in nums:
  
      temp = dp[:]
  
      for s in temp:
  
          new_sum = s + num
          
          # skip invalid states
          if s == float('-inf'):
              continue
  
          dp[new_sum % 3] = max(
              dp[new_sum % 3],
              new_sum
          )
  
  
  return dp[0]

Time Complexity - 3*N
Space Complexity - O(3) DP Array

