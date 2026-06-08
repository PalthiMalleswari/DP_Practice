#Problem - https://leetcode.com/problems/ones-and-zeroes/
# Refer Ones and Zeros.md File For Approach

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        
        le = len(strs)
        dp = {}
  
        def get_max_len(ind,z,o):

            if ind<0:
                return 0
            if (ind,z,o) in dp:
                return dp[(ind,z,o)]
            
            take = 0
            if z-strs[ind].count('0')>=0 and o-strs[ind].count('1')>=0:
                take = get_max_len(ind-1,z-strs[ind].count('0'),o-strs[ind].count('1'))+1
            dont = get_max_len(ind-1,z,o)
            
            dp[(ind,z,o)] = max(take,dont)
            return dp[(ind,z,o)]

        return get_max_len(le-1,m,n)

#Time Complexity - O(Len(Strs)*M*N)
#Space Complexity - O(len(strs)*m*n) + Recursion Call Stack Space

#======================= 3D Bottom Up Approach ===========

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        
        lenn = len(strs)
        dp = [[[0]*(n+1) for _ in range(m+1)] for _ in range(lenn+1)]

        for i in range(1,lenn+1):
            
            zeros = strs[i-1].count('0')
            ones = strs[i-1].count('1')

            for j in range(m+1):
                for k in range(n+1):
                    dp[i][j][k] = dp[i-1][j][k]

                    if j>=zeros and k>=ones:
                        dp[i][j][k] = max(dp[i][j][k],dp[i-1][j-zeros][k-ones]+1)

        return dp[lenn][m][n]

#Time Complexity - O(Len(Strs)*M*N)
#Space Complexity - O(len(strs)*m*n)

#=================== 2D Space Optimization Approach ==============

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        
        lenn = len(strs)
        dp = [[0]*(n+1) for _ in range(m+1)]

        for st in strs:
            
            zeros = st.count('0')
            ones = st.count('1')

            for j in range(m,zeros-1,-1):
                for k in range(n,ones-1,-1):
   
                        dp[j][k] = max(dp[j][k],dp[j-zeros][k-ones]+1)

        return dp[m][n]

Time Complexity - O(len(strs)*m*n)
Space Complexity - O(m*n)


