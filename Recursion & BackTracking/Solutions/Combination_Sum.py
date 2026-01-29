# Problem - https://leetcode.com/problems/combination-sum/description/

# Intution - Just Like We Generate Subsequences/Combinations, index by index

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        n = len(candidates)
        comb = []
        ans = []

        def generate_comb(ind,need):

            if need == 0:
                ans.append(comb[:])
        
            for st in range(ind,n):

                if candidates[st] <= need:
                    comb.append(candidates[st])
                    generate_comb(st,need-candidates[st])
                    comb.pop()

        generate_comb(0,target)

        return ans
          
        generate_comb(0,target)
        return res

# ============= Time Complexity ========================

🧠 Key Variables

n = number of candidates

T = target

m = smallest candidate value

Worst case depth happens when we keep picking the smallest number:

max depth ≈ T / m

🌳 Shape of Recursion Tree

At each level, loop runs up to n choices.

Height of tree ≈ T / m

So number of nodes is roughly:
n^(T/m)

This is exponential.

⏱️ Time Complexity - O(n^(T/m))
	​
Why?

Depth ≈ T/m

Each level branches up to n times

Copying combination costs O(T/m) as well

But we usually write:

Time = Exponential in (T/m)

# ========== Space Complexity =================
📦 Space Complexity

Two parts:

1️⃣ Recursion stack

Depth = T/m
O(T/m)

2️⃣ Combination storage

Each combination length ≤ T/m
If total valid combinations = K:
O(K×(T/m))

# ================= Other Way(Take & Not Take) =================

"""
Intution - Every Index has two possiblities Take,Not Take, if we Take,we can Take the Same Ele n times, so don't increament ind once you've taken a ele
           If you don't Take, Move to next index
"""
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
       
        ans = []
        n = len(candidates)
        comb = []
        def get_comb(ind,need):

            if ind >= n:
                return
            if need == 0:
                ans.append(comb[:])
                return
            
            # Take
            if candidates[ind]<=need:
                comb.append(candidates[ind])
                get_comb(ind,need-candidates[ind])
                comb.pop()
            
            # Not Take
            get_comb(ind+1,need)
        
        get_comb(0,target)
        return ans

Time Complexity - O(2^N)
Space Complexity - O(N+N)//Recursive Tree Depth+Ans
