# https://www.geeksforgeeks.org/dsa/longest-common-substring-dp-29/
# https://takeuforward.org/data-structure/longest-common-substring-dp-27

#  Naive Approach
n1 = len(str1)
n2 = len(str2)
res = 0

# Consider every pair of index and find the length
# of the longest common substring beginning with
# every pair. Finally return max of all maximums.

for i in range(n1):

  for j in range(n2):

    cur = 0

    while ((cur+i)<n1 and cur+j < n2 and str1[cur+i]==str2[cur+j]):

      cur+=1
    
    res = max(cur,res)

return res

# Time Complexity - O(n1*n2*min(n1.n2))
#  Space Complexity - O(1)

# Tabulation

def longest_common_substring(str1,str2):

  n1 = len(str1)
  n2 = len(str2)

  # Represents the length of the LCSub from 0 to i in str1 and 0 to j in str2 
  dp = [[0 for _ in range(n2+1)] for _ in range(n1+1)]

  ans = 0

  for i in range(1,n1):
    
    for j in range(1,n2):
      
      if str1[i-1] == str2[j-1]:
        
          dp[i][j] = dp[i-1][j-1]
          ans = max(ans,dp[i][j])
      
      else:
        
          dp[i][j] = 0
        
  return ans

# Time Complexity - O(N1*N2)
# Space Complexity  - O(N1*N2)

#  Space Optimization

"""
# If we observe the relation in the tabulation approach, we use dp[i-1][j-1] to calculate the present row. This means we are only using the previous row, dp[ind1-1][ ], to compute the current row.
# Since we only need the previous row to calculate the current row, we don't need to maintain the entire 2D dp array. Instead, we can use just two rows: prev (corresponding to dp[ind-1]) and cur (corresponding to dp[ind]).
"""
  ans = 0
  prev = [0]*(n2+1)
  cur = [0]*(n2+1)
  
  for i in range(1,n1):
    
    for j in range(1,n2):
      
        if str1[i-1] == str2[j-1]:
          
            cur[j] = prev[j-1]
            ans = max(ans,cur[j])
        
        else:
          
            cur[j] = 0
          
    prev = cur
        
  return ans
    
