#  Problem - https://leetcode.com/problems/delete-operation-for-two-strings/description/
"""
Find Length of Longest Common Subsequence(LLCS) - x
n1 = len(word1)
n2 = len(word2)
ans = (n1-x)+(n2-x)
"""

#  Memorization

#  Time Complexity - O(N1*N2)
#  Space Complexity (Dp Array) - O(N1*N2)

class Solution:
    def minDistance(self, word1: str, word2: str) -> int: 
        
        n1 = len(word1)
        n2 = len(word2)

        dp = [[-1]*n2 for _ in range(n1)]

        def get_llcsubseq(ind1,ind2):

            if ind1 < 0 or ind2 < 0:
                
                return 0

            if dp[ind1][ind2] != -1:
                
                return dp[ind1][ind2]
                
            if word1[ind1] == word2[ind2]:

                dp[ind1][ind2] = 1 + get_llcsubseq(ind1-1,ind2-1)
                return dp[ind1][ind2]

            else:

                dp[ind1][ind2] =  max(get_llcsubseq(ind1-1,ind2),get_llcsubseq(ind1,ind2-1))
                
                return dp[ind1][ind2]        
        
        ans = get_llcsubseq(n1-1,n2-1)

        return (n1-ans)+(n2-ans)
