# Problem - https://leetcode.com/problems/longest-increasing-subsequence/description/

#========== Recursive Memorized Top Down ==========
  dp = {}
  def max_len(ind,prev):
      
      if ind >=n:
          return 0
      if (ind,prev) in dp:
          return dp[(ind,prev)]
      ans = float('-inf')
      for i in range(ind+1,n):
          if prev<nums[i]:
              ans = max(ans,max_len(i,nums[i]))
      
      dp[(ind,prev)] = 0 if ans == float('-inf') else ans+1
      
      return dp[(ind,prev)]
  return max_len(-1,float('-inf'))

Time Complexity - O(N*N)
Space Complexity - O(N*N)+ Recursive Stack Space

#========== Recursive Memorized Bottom Up Down ==========

  def max_len(ind,prev_ind):
      
      if ind <0:
          return 0
      if (ind,prev_ind) in dp:
          return dp[(ind,prev_ind)]
      ans = float('-inf')
      for i in range(ind-1,-1,-1):
          if prev_ind==float('inf') or nums[prev_ind]>nums[i]:
              ans = max(ans,max_len(i,i))
      
      dp[(ind,prev_ind)] = 0 if ans == float('-inf') else ans+1
      return dp[(ind,prev_ind)]

  return max_len(n,float('inf'))

Time Complexity - O(N*N)
Space Complexity - O(N*N)+ Recursive Stack Space

#============= Optimized Approach ============
    n = len(nums)
    dp = [1]*n

    for i in range(n):
        for j in range(i):
            if nums[j]<nums[i]:
                dp[i] = max(dp[i],dp[j]+1)
    return max(dp)

Time Complexity - O(N*N)
Space Complexity - O(N)
