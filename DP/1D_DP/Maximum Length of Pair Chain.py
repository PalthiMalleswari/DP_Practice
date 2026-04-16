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
