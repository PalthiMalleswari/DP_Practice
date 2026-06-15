# Problem - https://leetcode.com/problems/perfect-squares/

"""
Here the Optimal Bound is squareroot(n) not n/2  
Square root of n is = (n)^1/2 = (n**0.5)
"""
class Solution:
    def numSquares(self, n: int) -> int:
        
        dp = {}

        def cal_min_no(new_nn):
        
            if new_nn <=1:
                return new_nn

            if new_nn in dp:
                return dp[new_nn]

            bnd = new_nn//2
            cnt = float('inf')
            
            for i in range(1,bnd+1):
                if new_nn >= (i*i):

                    p = cal_min_no(new_nn-(i*i))
                    cnt=min(cnt,p+1)
                    
            dp[new_nn] = cnt
            return cnt

        return cal_min_no(n)
Time Complexity - O(N*(N/2)) + Recursive Stack Space
Space Complexity - O(N)
#==================== Optimal Approach ======================


        dp = [float('inf')]*(n+1)
        dp[0] = 0

        for i in range(n+1):
            for j in range(1,int(i**0.5)+1):
                if j*j <=i:
                    dp[i] = min(dp[i],dp[i-(j*j)]+1)

        return dp[n]

Time Complexity - O(N*root(N))
Space Complexity - O(N)


