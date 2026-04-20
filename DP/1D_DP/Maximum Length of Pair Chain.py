# Problem - https://algomaster.io/learn/dsa/maximum-length-of-pair-chain


# =============== Intial Approach ==============

1. Sort By end Value
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
    
        pairs = sorted(pairs,key =lambda tup:tup[0])
        n = len(pairs)
        
        def find_max_len(ind,prev_end):
            if ind >= n:
                return 0
            ans = 0
            for i in range(ind,n):
                
                if prev_end < pairs[i][0]:                    
                    ans = max(ans,find_max_len(i+1,pairs[i][1])+1)
                   
            return ans
        return find_max_len(0, float("-inf"))

# Take/Not Take Approach =============

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        
        
        pairs = sorted(pairs,key =lambda tup:tup[0])
        pairs = [(float('-inf'),float('-inf'))] + pairs

        n = len(pairs)
        def dfs(index):
            if index == n:
                return 0

            # skip
            not_take = dfs(index + 1)

            # take
            take = 0
            if pairs[index-1][1] < pairs[index][0]:
                take = 1 + dfs(index + 1)

            return max(take, not_take)
        return dfs(1)

Time Complexity - O(2^N)
Space Complexity - O(N) Recursion Call Stack

# ============= Memorization ==================
If we use States as (index,prev_end) prev_end should be Max(Nums) Which wastes lot of memory So Optimal State selection is (index,prev_index) 

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
    
        pairs = sorted(pairs,key =lambda tup:tup[0])
        n = len(pairs)
        memo = {}
        
        def find_max_len(ind,prev_ind):
            if ind >= n:
                return 0
            
            if (ind,prev_ind) in memo:
                return memo[(ind,prev_ind)]

            ans = 0
            for i in range(ind,n):
                
                if prev_ind == -1 or pairs[prev_ind][1] < pairs[i][0]:
                    
                    ans = max(ans,find_max_len(i+1,i)+1)

            memo[(ind,prev_ind)] = ans
            return ans
            
        return find_max_len(0,-1)
        
#============ Different Way Of Memorization =======

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
    
        pairs = sorted(pairs,key =lambda tup:tup[0])
        n = len(pairs)
        memo = {}
        from functools import lru_cache
        @lru_cache(None)
        
        def find_max_len(ind,prev_ind):
            if ind >= n:
                return 0
            
            ans = 0
            for i in range(ind,n):
                
                if prev_ind == -1 or pairs[prev_ind][1] < pairs[i][0]:
                    
                    ans = max(ans,find_max_len(i+1,i)+1)
                   
            return ans
        return find_max_len(0,-1)

Time Complexity - O(N*N)
Space Complexity - O(N*N(Memorization)+N(Recursion Stack Space))

# ==================== Bottom Up ==============

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        
        pairs.sort()
        n = len(pairs)
        dp = [1]*n

        for i in range(1,n):
            for j in range(i):
                if pairs[j][1] < pairs[i][0]:
                    dp[i] = max(dp[i],dp[j]+1)
        return dp[n-1 (We can return  max(dp))
        
Time Complexity - O(N*N)
Space Complexity - O(N)

#============ Optimal Solution (Greedy) =================

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        
        pairs.sort(key=lambda x: x[1])
        n = len(pairs)
        count = 1
        prev_end = pairs[0][1]

        for i in range(1,n):
            if prev_end <pairs[i][0]:
                count += 1
                prev_end = pairs[i][1]
        return count
Time Complexity - O(NlogN)
Space Complexity - O(1)

