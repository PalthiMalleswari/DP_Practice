#Problem - https://leetcode.com/problems/distinct-subsequences/description/

        def is_possible(i,j):

            if j>=n2:
                return 1
            if i>=n1 and j<n2:
                return 0
            
            take,dont = 0,0
            if (i,j) in memo:
                return memo[(i,j)]
            
            if s[i] == t[j]:

                take = is_possible(i+1,j+1)+is_possible(i+1,j)

            else:
                dont = is_possible(i+1,j)

            memo[(i,j)] = take+dont
            return memo[(i,j)]

        return is_possible(0,0)

Time Complexity - O(N*M)
Space Complexity - O(N*M)

#=============== Optimized ==============

  n1 = len(s)
  n2 = len(t)
  memo = {}

  dp = [[-1]*(n2+1) for _ in range(n1+1)]

  for i in range(n1+1):

      dp[i][0] = 1

  for j in range(1,n2+1):

      dp[0][j] = 0


  for i in range(1,n1+1):
      for j in range(1,n2+1):

          if s[i-1] == t[j-1]:

              c1 = dp[i-1][j-1]
              c2 = dp[i-1][j]

              dp[i][j] = c1+c2

          else:
              dp[i][j] = dp[i-1][j]
  
  return dp[n1][n2]
