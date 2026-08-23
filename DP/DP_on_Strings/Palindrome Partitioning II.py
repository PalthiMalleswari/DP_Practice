#Problem - https://leetcode.com/problems/palindrome-partitioning-ii/description/

class Solution:
    def minCut(self, s: str) -> int:
        
        n = len(s)

        is_palindrome = [[False]*n for _ in range(n)]

        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if s[i]==s[j] and (j-i<=2 or is_palindrome[i+1][j-1]):
                    is_palindrome[i][j] = True
        
        cuts = [0]*n
        for i in range(n):

            if is_palindrome[0][i]:
                cuts[i] = 0
                continue
            cuts[i] = i
            for j in range(1,i+1):
                if is_palindrome[j][i]:
                    cuts[i] = min(cuts[i],cuts[j-1]+1)
        return cuts[n-1]


Time Complexity - O(N*N)
Space Complexity - O(N*N)
