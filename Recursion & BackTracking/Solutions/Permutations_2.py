# Problem - https://leetcode.com/problems/permutations-ii/description/


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        n = len(nums)
        res = []
        perm = []
        visited = [False] * n

        def backtrack():
            if len(perm) == n:
                res.append(perm[:])
                return

            for i in range(n):

                # Rule 1 — cannot reuse same index
                if visited[i]:
                    continue

                # Rule 2 — skip duplicate values at same tree level
                if i > 0 and nums[i] == nums[i-1] and not visited[i-1]:

                    continue

                visited[i] = True
                perm.append(nums[i])
                backtrack()
                perm.pop()
                visited[i] = False

        backtrack()
        return res

  Time Complexity - O(N!)
Space Complexity - O(N+N)//Recursive Max Depth+Result

# ================== Other Different Way =====================


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        perm,ans = [],[]
        visited = []
        nums.sort()

        def generate_perms():

            if len(perm) == n:
                ans.append(perm[:])
                return
            else:
                i = 0
                while i < n:

                    if i in visited:
                        i += 1
                        continue
                    perm.append(nums[i])
                    visited.append(i)
                    generate_perms()
                    perm.pop()
                    visited.pop()

                    if i+1 < n and nums[i] == nums[i+1]:

                        while i+1 < n and nums[i] == nums[i+1]:
                            
                            i += 1

                    i+=1

        generate_perms()
        return ans
