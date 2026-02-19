# Problem - https://leetcode.com/problems/combination-sum-iv/description/


# ======== BF(Pure Recursion) ================

        n = len(nums)
        def get_comb(tar):

            if tar == 0:
                return 1       
            cnt = 0 
            for i in range(n):

                if tar>=nums[i]:
                    cnt += get_comb(tar-nums[i])
            return cnt
        return get_comb(target)

Without memoization:

This is roughly: O(n^target)

It behaves like exponential growth.
Why?
Because:
At each level → you try n choices
Depth ≈ target (if nums contains 1)
So worst case: O(n^target)

Space Complexity -> O(target) Stack space


# =========== Memorization ==============

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        dp = [-1]*(target+1)
        def get_comb(tar):
            if tar == 0:
                return 1
              
            if dp[tar] != -1:
                return dp[tar]
              
            cnt = 0 
            for i in range(n):
                if tar>=nums[i]:
                    cnt += get_comb(tar-nums[i])
                  
            dp[tar] = cnt
            return dp[tar]
          
        return get_comb(target)
Time Complexity -> 
Unique states = target

For each state → loop through n numbers
Time=O(n×target)

Space:

Memo table → O(target)

Recursion stack → O(target)
