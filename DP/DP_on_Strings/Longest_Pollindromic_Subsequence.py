
#  Problem - https://leetcode.com/problems/longest-palindromic-subsequence/


# Bottom Up/Memorization

l = len(s)

dp = [[-1 for _ in range(l)] for _ in range(l)]

def get_llcp(ind1,ind2):

    if ind1 < l and ind2 >= 0 and ind1 > ind2:
        dp[ind1][ind2] = 0
        return dp[ind1][ind2]
    
    if ind1 == ind2 and ind1 < l and ind2 >=0 :
        dp[ind1][ind2] = 1
        return dp[ind1][ind2]

    if dp[ind1][ind2] != -1:
        return dp[ind1][ind2]

    if s[ind1] == s[ind2]:

        dp[ind1][ind2] = 2+get_llcp(ind1+1,ind2-1)
        return dp[ind1][ind2]

    else:

        c1 = get_llcp(ind1+1,ind2)
        c2 = get_llcp(ind1,ind2-1)

        dp[ind1][ind2] = max(c1,c2)

        return dp[ind1][ind2]

return get_llcp(0,l-1)

#  Time Complexity - O(N*N)
# Space Complexity(Stack Space) - O(N+N)



# Bottom Up 

l = len(s)

dp = [[0 for _ in range(l)] for _ in range(l)]

 for i in range(l-1,-1,-1):

            dp[i][i] = 1

            for j in range(i+1,l):

                if s[i] == s[j]:

                    dp[i][j] = dp[i+1][j-1] + 2
                else:

                    dp[i][j] = max(dp[i+1][j],dp[i][j-1])
        
return dp[0][l-1]
 #  Time Complexity - O(N*N)
# Space Complexity(Dp Array) - O(N+N)       
        
