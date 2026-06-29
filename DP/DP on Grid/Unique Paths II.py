#Problem - https://leetcode.com/problems/unique-paths-ii/description/

    n = len(obstacleGrid)
    m = len(obstacleGrid[0])

    memo = {}

    def find_all_paths(r,c):

        if r>=n or c>=m or obstacleGrid[r][c]:
            return 0
        
        if r==n-1 and c ==m-1:
            return 1
        
        if (r,c) in memo:
            return memo[(r,c)]
        right = find_all_paths(r,c+1)
        dwn = find_all_paths(r+1,c)
        
        memo[(r,c)] = right+dwn
        return memo[(r,c)]

    return find_all_paths(0,0)

Time Complexity - O(N*M)
Space Complexity - O(N*M) + (N*M) Recursive Stack Space

#============= 2D Optimization =====================

        dp = [[0]*m for _ in range(n)]

        dp[0][0] = 0 if obstacleGrid[0][0] else 1

        for i in range(n):

            for j in range(m):
                
                if (i==0 and j==0):
                    continue

                if obstacleGrid[i][j]:
                    continue

                if i==0 and j-1>=0:

                    dp[i][j] = dp[i][j-1]

                elif j==0 and i-1>=0:

                    dp[i][j] = dp[i-1][j]

                else:

                    dp[i][j] = dp[i-1][j]+dp[i][j-1]

        return dp[n-1][m-1]

Time Complexity - O(N*M)
Space Complexity - O(N*M)

#===================== 1D optimized Approach =============

        dp = [0]*m

        dp[0] = 0 if obstacleGrid[0][0] else 1

        for i in range(n):

            for j in range(m):
                
                if (i==0 and j==0):
                    continue

                if obstacleGrid[i][j]:
                    dp[j] = 0
                    continue

                if j-1>=0:

                    dp[j] = dp[j]+dp[j-1]

        return dp[m-1]

Time Complexity - O(N*M)
Space Complexity - O(M)

