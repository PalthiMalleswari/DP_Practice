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
        
        


