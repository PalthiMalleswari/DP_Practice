# Problem - https://leetcode.com/problems/permutations/

# =============== Intuition ===========

"""
At Every Level, choose ele which are not visied, Recursively
"""

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
       
        ans = []

        n = len(nums)
        
        def get_perm(perm):

            if len(perm)==n:
                ans.append(perm[:])
            
            for e in nums:

                if e not in perm:

                    perm.append(e)

                    get_perm(perm)

                    perm.pop()

        get_perm([])
        return ans

Space Complexity - O(N+N)//Ans+Recursive Call Stack Space
Time Complexity - O(N!)

Example:[1,2,3]
index - 0 -> 3 possible choices (1,2,3)
index - 1 -> 2 possible choices (index-0 already fixed)
index - 2 -> 1 possible choices (index-0,1 already fixed)
