# Problem - https://leetcode.com/problems/subsets/

#  Intuition: Every Element has Pick or not pick option 

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        ans = []
        n = len(nums)
        
        def find_all_subsets(ind,cur_path):

            if ind >= n:
                ans.append(cur_path[:])
                return
            
            #  Pick 
            cur_path.append(nums[ind])
            find_all_subsets(ind+1,cur_path)
            cur_path.pop()

            # Not Pick
            find_all_subsets(ind+1,cur_path)
        
        find_all_subsets(0,[])

        return ans
            
        
Time Complexity - O(2^N)
Space Complexity - O(N+N) // Cur Path to Store Ans + Recursion Stack space (Maximum Depth of the Recursion)

# ========= Other Different Way ====================

#  Intuition: At every ind traverse on subsets start with this index and Collect paths

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        ans = []
        n = len(nums)
        
        def find_all_subsets(ind,cur_path):

            
            ans.append(cur_path[:])
            
            if ind>=n:
                return

            for i in range(ind,n):

                cur_path.append(nums[i])

                find_all_subsets(i+1,cur_path)

                cur_path.pop()

            
        find_all_subsets(0,[])

        return ans

Time Complexity - O(2^N)
Space Complexity - O(N) // For Stack Space (Maximum Recursion Depth)
