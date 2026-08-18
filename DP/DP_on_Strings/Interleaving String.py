#Question - https://leetcode.com/problems/interleaving-string/description/

#=================== BF ===================

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        n1 = len(s1)
        n2 = len(s2)
        n3 = len(s3)
        memo = {}

        def is_possible(i,j,k):

            if i>=n1 and j>=n2 and k<n3:
                return False
            if k>=n3 and i>=n1 and j>=n2:
                return True
            if (i,j,k) in memo:
                return memo[(i,j,k)]
 
            
            if i<n1 and k<n3 and s3[k] == s1[i]:

                if is_possible(i+1,j,k+1):
                    memo[(i,j,k)] = True
                    return True

            if j<n2 and k<n3 and s3[k] == s2[j]:

                if is_possible(i,j+1,k+1):
                    memo[(i,j,k)] = True
                    return True

            memo[(i,j,k)] = False
            return False
        return is_possible(0,0,0)

  Time Complexity - O(M*N)
  Space Complexity - O(M*N1*N2)

#=============== State Optimization ==================

# Here K always equals to i+j
      
        if n1+n2!=n3:
            return False

        def is_possible(i,j):

            if i<0 and j<0:
                return True

            if (i,j) in memo:
                return memo[(i,j)]
 
            res = False

            if i>=0 and s3[i+j+1] == s1[i]:

                res = is_possible(i-1,j)

            if not res and j>=0 and s3[i+j+1] == s2[j]:

                res = is_possible(i,j-1)
                    

            memo[(i,j)] = res
            return res

        return is_possible(n1-1,n2-1)

Time Complexity  - O(M*N)
Space Complexity - O(M*N)+Stack Space

#=============== Space Optimization and Optimal Approach  =================

  dp = [False]*(n2+1)

        dp[0] = True
        
        for j in range(1,n2+1):

            dp[j] = dp[j-1] and s2[j-1] == s3[j-1]

        for i in range(1,n1+1):
            
            dp[0] = dp[0] and s1[i-1]==s3[i-1] 

            for j in range(1,n2+1):

                dp[j] = dp[j-1] and s2[j-1] == s3[i+j-1] or \
                            dp[j] and s1[i-1] == s3[i+j-1]
  
        return dp[n2]
Time Complexity - O(M*N)
Space Complexity - O(N)

