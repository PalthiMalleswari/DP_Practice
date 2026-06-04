"""
Problem - https://leetcode.com/problems/partition-equal-subset-sum/description/

Given an integer array nums, return true if you can partition the array into two subsets 
such that the sum of the elements in both subsets is equal or false otherwise.

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].

"""
"""
dp[ind][tareget] denotes that, is there exist a subset with sum = target from 0 to ind
"""

#=========   Intial Brute Force(MLE) =============

total = sum(nums)
memo = {}

if total%2 != 0:
    return False

def can_partition(ind,rem):

    if rem==0:
        return True

    if ind>=len(nums) or rem<0:
        return False   
                 
    if (ind,rem) in memo:
        return memo[(ind,rem)]
    
    n = can_partition(ind+1,rem)
    t = can_partition(ind+1,rem-nums[ind])

    memo[(ind,rem)] =  n or t
    return  memo[(ind,rem)] 

return can_partition(0,total//2)


def canPartition(self, nums: List[int]) -> bool:

    s = sum(nums)
    n = len(nums)

    if s%2 != 0:
        return False
      
    target = s//2
    dp = [[-1 for j in range(target+1)] for i in range(n)]
    
    def get_partion(ind,target):
        if ind == 0 :
            return nums[ind] == target
        if dp[ind][target] != -1:
            return dp[ind][target]
    
        boolTake = False
        
        not_bool = get_partion(ind-1,target)
        if nums[ind]<=target:
            boolTake = get_partion(ind-1,target-nums[ind]
        dp[ind][target] =  boolTake or not_bool
        return dp[ind][target]
      
    return get_partion(n-1,target)


#================ 2D DP Appraoch ================

class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        total = sum(nums)
        if total%2:
            return False

        n = len(nums)
        target = total//2
        dp = [[False]*(target+1) for _ in range(n)]
        
        for i in range(n):
            dp[i][0] = True

        for i in range(1,n):
            for rem_s in range(target,-1,-1):
                take = False
                dt = False
                
                if i-1>=0 and rem_s>=nums[i]:
                    take =  dp[i-1][rem_s-nums[i]]
                if i-1>=0:
                    dt = dp[i-1][rem_s]
                    
                dp[i][rem_s] = dt or take
        
        return dp[n-1][target]
        
Time Complexity - O(n*target)
Space Complexity - O(n*target)

#================= Space Optimized Approach ================

class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        total = sum(nums)
        if total%2:
            return False

        n = len(nums)
        target = total//2
        dp = [False]*(target+1)

        dp[0] = True

        for i in range(n):
            for rem_s in range(target,-1,-1):
                take = False                
                if rem_s>=nums[i]:
                    take =  dp[rem_s-nums[i]]
                dt = dp[rem_s]
                dp[rem_s] = dt or take
        
        return dp[target]

Time Complexity - O(N*target)
Space Complexity - O(target)

#===== a slite condiiton varition To avoid negative values =====

class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        total = sum(nums)
        if total%2:
            return False

        n = len(nums)
        target = total//2
        dp = [False]*(target+1)

        dp[0] = True

        for i in range(n):
            for rem_s in range(target,nums[i]-1,-1):

                take =  dp[rem_s-nums[i]]
                dt = dp[rem_s]
                dp[rem_s] = dt or take
        
        return dp[target]
        

