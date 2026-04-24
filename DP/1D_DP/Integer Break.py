# Problem - https://leetcode.com/problems/integer-break/description/

class Solution:
    def integerBreak(self, n: int) -> int:
        split = n//2+1
        ans = 0
        
        if n==2 :
            return 1
        memo = {} 
        def find_max(ind):
            if ind == 0:
                return 1
            
            if ind in memo:
                return memo[ind]

            max_val = 0
            for i in range(1, split + 1):
                if ind - i >= 0:
                    max_val = max(max_val, i * find_max(ind - i))
            
            memo[ind] = max_val
            return memo[ind]

        return find_max(n)

Time Complexity - O(2^N)
Space Complexity - O(N+N)

#================== Brute Force 1 ==================

class Solution:
    def integerBreak(self, n: int) -> int:
        
        memo = {} 
        def find_max(ind):
            if ind == 0:
                return 1
            
            if ind in memo:
                return memo[ind]

            max_val = 0
            for i in range(1, ind):
                if ind - i >= 0:
                    max_val = max(max_val,  i * (ind - i), i * find_max(ind - i))
                    
            memo[ind] = max_val
            return memo[ind]

        return find_max(n)
Time Complexity - O(2^N)
Space Complexity - O(N+N)

#================== Bottom Up Solution ====================

class Solution:
    def integerBreak(self, n: int) -> int:
        
        dp = [0]*(n+1)
        dp[1] = 1
        for num in range(2,n+1):
            for i in range(1,num):
                dp[num] = max(dp[num],i*(num-i),i*dp[(num-i)])
        return dp[n]

  Time Complexity - O(N*N)
Space Complexity - O(N)
