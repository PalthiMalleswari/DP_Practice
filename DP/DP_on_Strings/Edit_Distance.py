#Problem - https://leetcode.com/problems/edit-distance/description/

#============================= Intial Approach (0-indexed) Top Down ===================

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        n,m = len(word1),len(word2)
        memo = {}

        def find_min_dis(i,j):
            
            if i==-1 and j==-1:
                return 0

            if i==-1:
                return j+1
            if j==-1:
                return i+1
            
            if (i,j) in memo:
                return memo[(i,j)]
            
            
            if word1[i]==word2[j]:
                memo[(i,j)] = find_min_dis(i-1,j-1)
            else:

                delete = find_min_dis(i-1,j)
                insert = find_min_dis(i,j-1)
                update = find_min_dis(i-1,j-1)

                memo[(i,j)] = min(delete,insert,update)+1
            
            return memo[(i,j)]
        return find_min_dis(n-1,m-1)

  #Time Complexity - O(M*N)
  #Space Complexity - O(M*N)

#============================= 1 based Index Appraoch (Top Down Appraoch) ==============

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        n,m = len(word1),len(word2)
        memo = {}

        def find_min_dis(i,j):

            if i==0:
                return j
            if j==0:
                return i
            
            if (i,j) in memo:
                return memo[(i,j)]
            
            
            if word1[i-1]==word2[j-1]:
                memo[(i,j)] = find_min_dis(i-1,j-1)
            else:

                delete = find_min_dis(i-1,j)
                insert = find_min_dis(i,j-1)
                update = find_min_dis(i-1,j-1)

                memo[(i,j)] = min(delete,insert,update)+1
            
            return memo[(i,j)]
        return find_min_dis(n,m)

  #Time Complexity - O(M*N)
  #Space Complexity - O(M*N)

#========================= Bottom up Approach =======================

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        n1,n2 = len(word1),len(word2)
        
        dp = [[0]*(n2+1) for _ in range(n1+1)]

        for i in range(n1+1):
            dp[i][0] = i

        for j in range(n2+1):
            dp[0][j] = j
        
        for i in range(1,n1+1):

            for j in range(1,n2+1):

                if word1[i-1]==word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1],dp[i][j-1],dp[i-1][j])+1

        return dp[n1][n2]

# Time Complexity - O(M*N)
# Space Complexity - O(M*N)

