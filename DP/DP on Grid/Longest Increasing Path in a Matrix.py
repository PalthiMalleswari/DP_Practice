#Problem - https://leetcode.com/problems/longest-increasing-path-in-a-matrix/description/

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m,n = len(matrix),len(matrix[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        dp = [[0]*n for _ in range(m)]

        def dfs(i,j):

            if dp[i][j] !=0:
                return dp[i][j]

            best = 1
            for dr,dj in dirs:
                ni,nj = dr+i,dj+j
                if 0<=ni<m and 0<=nj<n and matrix[i][j] <matrix[ni][nj]:
                    best = max(best,1+dfs(ni,nj))
            dp[i][j] = best
            return best
        
        result = 0
        for i in range(m):
            for j in range(n):
                result = max(result,dfs(i,j))
        return result

Time Complexity - O(M*N)
Space Complexity - O(M*N)
