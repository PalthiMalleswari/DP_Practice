# Problem - 

# Intution -  Remove duplicate choices at every level, Sort an Array, while taking a ele, 
#             check if next elememt is same as previous, if yes, then take last occurence of the ele to avoid duplicate subsets  

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        ans = []
        n = len(nums)

        def get_subset_2(ind,path):

            if ind == n:
                ans.append(path[:])
                return
            
            while ind+1< n and nums[ind] == nums[ind+1]:
                ind += 1
                
            path.append(nums[ind])
            get_subset_2(ind+1)
            subarr.pop()

            subset_ii(ind+1)

        
        get_subset_2(0,[])
        return ans

Time Complexity - O(2^N)
Space Complexity - O(N) // Maximum Recursive Tree Depth

# ================ Other Way ================

# Intution - Remove Dedundent Choices at each level by sorting inp array,duplicate choices allowed for different levels but not in same level

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        ans = []
        n = len(nums)

        def get_subset_2(ind,path):

            ans.append(path[:])

            for i in range(ind,n):

                if i>ind and nums[i]==nums[i-1]:
                    continue
                path.append(nums[i])
                get_subset_2(i+1,path)
                path.pop()

        get_subset_2(0,[])
        return ans
      
Time Complexity - O(2^N)
Space Complexity - O(N) // Maximum Recursive Tree Depth
