# Question - https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/description/

"""
Find Lenght of Longest Palindrome in string(LLP) and then do ->  Total string Lenght(n) - llp
"""
# Memorization
#  Time Complexity - O(N*N) where N - length of string
#  Space Complexity (Dp Array) - O(N*N)

class Solution:
    def minInsertions(self, s: str) -> int:
        
        n = len(s)

        dp = [[-1]*n for _ in range(n)]

        def get_llp(ind1,ind2):

            if ind1>ind2 or ind1 >=n and ind2 <0:
                dp[ind1][ind2] = 0
                return dp[ind1][ind2]

            if dp[ind1][ind2] != -1:
                return dp[ind1][ind2]
                
            if ind1 == ind2:
                
                dp[ind1][ind2] = 1
                return dp[ind1][ind2]
            
            if s[ind1]==s[ind2]:

                dp[ind1][ind2] = get_llp(ind1+1,ind2-1)+2
                return  dp[ind1][ind2]
            
            else:

                dp[ind1][ind2] =  max(get_llp(ind1+1,ind2),get_llp(ind1,ind2-1))

                return dp[ind1][ind2]

        ans = get_llp(0,n-1)

        return n-ans
