# Question - https://leetcode.com/problems/longest-common-subsequence/description/


# Naive Approach
# get_lcs(ind1,ind2) denotes length of Longest Common subsequence(LCS) of text1[0..ind1] and text2[0..ind2]
# It has Overlapping subproblem
# Time Complexity  - O(2^m)*O(2^n) = O(2^(n+m)
# Space Complexity(Stack Space)- O(n*m) Explnation here - https://chatgpt.com/c/694379a2-3f24-8321-88d3-dc931be82e06
# For each index in text1 we are comparing with each index of text2 at worst case if there are no match
# But as we're doing alternative reduction over indexes (at least one index reduction at each call) hence it's O(n+m)

def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    n = len(text1)
    m = len(text2)

    def get_lcs(ind1,ind2):
        if ind1 < 0 or ind2 < 0:
          return 0
      
        if text1[ind1] == text2[ind2]:
            return get_lcs(ind1-1,ind2-1)+1
        else:
          return max(get_lcs(ind1,ind2-1),get_lcs(ind1-1,ind2))
    
    return get_lcs(n-1,m-1)


# It has Overlapping subproblem
# Memorization/Top Down approach
# dp[ind1,ind2] denotes length of Longest Common subsequence(LCS) of text1[0..ind1] and text2[0..ind2]
# Time Complexity - O(n*m)
# Space Complexity(DP Table & Recursive Stack Space) - O(n*m)+O(n+m)
      
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        n = len(text1)
        m = len(text2)

        dp = [ [-1 for _ in range(m)] for _ in range(n)]

        def get_lcs(ind1,ind2):

            if ind1 < 0 or ind2 < 0 :

                return 0
            
            if dp[ind1][ind2] != -1:

                return dp[ind1][ind2]
            
            if text1[ind1] == text2[ind2]:

                dp[ind1][ind2] = 1+get_lcs(ind1-1,ind2-1)

            else:

                dp[ind1][ind2] = max(get_lcs(ind1-1,ind2),get_lcs(ind1,ind2-1))
                
            return dp[ind1][ind2]
          
        return get_lcs(n-1,m-1)
      
# Bottom up/Tabulation
# Here as index goes to negative, we can't store them in arrays, we'll do index shifting to right by 1
#  ind = n => text1[n-1]
#  ind = 1 => text1[0] 
#  Base Case dp[i][0] and dp[0][j] = 0
# Time Complexity = O(N*M)
# Space Complexity = O(N*M)

  dp = [ [-1 for _ in range(m+1)] for _ in range(n+1)]

  for i in range(n+1):
      dp[i][0] = 0

  for j in range(m+1):
      dp[0][j] = 0

  for i in range(1,n+1):

      for j in range(1,m+1):

          if text1[i-1] == text2[j-1]:

              dp[i][j] = dp[i-1][j-1]+1
          else:

              dp[i][j] = max(dp[i-1][j],dp[i][j-1])
            
  return dp[n][m]

# We Can Optimize the space complexity Tooo !!!!!!
  
