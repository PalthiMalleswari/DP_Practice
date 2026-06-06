## Quesion -  https://leetcode.com/problems/target-sum/description/

# Solution

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        dp = {}

        def evaluate_expression(ind,cur_sum):

            if ind < 0 and cur_sum ==  target:

                dp[(ind,cur_sum)] = 1
                return dp[(ind,cur_sum)]
            
            if ind < 0 and cur_sum !=  target:

                dp[(ind,cur_sum)] = 0
                return dp[(ind,cur_sum)]
            
            if (ind,cur_sum) in dp:
                return dp[(ind,cur_sum)]

            # + possibility
            c1 = evaluate_expression(ind-1,cur_sum+nums[ind])

            # - possibility
            c2 = evaluate_expression(ind-1,cur_sum-nums[ind])

            dp[(ind,cur_sum)] = c1 + c2
                
            return dp[(ind,cur_sum)]

        n = len(nums)
        return evaluate_expression(n-1,0)
# Time Complexity - O(n*target)
#  For each index , at worst case,we'll have 0 to target states  
# Space Compexity - O(n*target)
        
        
#=========== Counter Approach (Tracks All possible sum from previous states)============
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        counter = {0:1}

        for num in nums:
            temp = {}

            for s,cnt in counter.items():
                temp[s+num] = temp.get(s+num,0)+cnt
                temp[s-num] = temp.get(s-num,0)+cnt
            counter = temp
        return counter.get(target,0)
        
Time Complexity - (n*(2*totalsum)) (Total positive and negative numbers too)
Space Complexity - O(n*2*totalsum) 

#================== 1D Optimized Approach =====================

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        ts = sum(nums)
        tar = (ts+target)//2

        if (ts+target)%2 or ts+target<0:
            return 0
        
        dp = [0]*(tar+1)
        dp[0] = 1

        for num in nums:
            for s in range(tar,-1,-1):
                if s>=num:
                    dp[s] += dp[s-num]

        return dp[tar]
        
Time Complexity - O(n*tar)
Space Complexity - O(target)
    
