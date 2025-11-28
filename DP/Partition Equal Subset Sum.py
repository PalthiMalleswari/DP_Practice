"""
Given an integer array nums, return true if you can partition the array into two subsets 
such that the sum of the elements in both subsets is equal or false otherwise.

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].

"""

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
