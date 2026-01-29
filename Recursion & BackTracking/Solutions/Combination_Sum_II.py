# Problem - https://leetcode.com/problems/combination-sum-ii/description/

# Intuition - Remove Duplicate Choices At Same Level

candidates = [1,1,2,5]
target = 3

          []
        /    \
       1      1  ❌ duplicate start
      /        \
     2          2


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        n = len(candidates)
        candidates.sort()
       
        ans = []
        comb = []

        def get_comb_2(ind,need):
            
            if need == 0:
                ans.append(comb[:])
                return
    
            for i in range(ind,n):
              
                """
                If this value is same as previous AND we are at the same recursion depth, skip it
                """
                if i>ind and candidates[i]==candidates[i-1]:
                    continue
                  
                if candidates[i]>need:
                    continue
                
                comb.append(candidates[i])
                get_comb_2(i+1,need-candidates[i])
                comb.pop()
        
        get_comb_2(0,target)
        return ans


        get_comb_2(0,target)
        return ans
            
Time complexity - O(2^N)
Space Complexity - O(N+N)//Recursion depth+Comb Array


# =========== Not Ideal+Not Optimal One =============

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        n = len(candidates)
        candidates.sort()
        visited = [False]*n
        ans = []
        comb = []

        def get_comb_2(ind,need):
            
            if need == 0:
                ans.append(comb[:])
                return

            if ind>=n:
                return

            print(ind)
            for st in range(ind,n):
                
                if st>0 and candidates[st]==candidates[st-1] and not visited[st-1]:
                    continue
                if candidates[st]>need:
                    continue
                comb.append(candidates[st])
                visited[st] = True
                get_comb_2(st+1,need-candidates[st])
                visited[st] = False
                comb.pop()

        get_comb_2(0,target)
        return ans
Time complexity - O(2^N)
Space Complexity - O(N+N+N)//Recursion depth+Comb Array+Visited Arr
