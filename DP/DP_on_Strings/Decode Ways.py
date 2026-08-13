#Problem - https://leetcode.com/problems/decode-ways/description/

class Solution:
    def numDecodings(self, s: str) -> int:
        
        n = len(s)
        valid = set([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26])
        memo = {}

        def num_decode_ways(ind):

            if ind>=n:
                return 1
            val = int(s[ind])
            if val ==0:
                return 0
            if ind in memo:
                return memo[ind]
            ans = 0
            if ind+1<n and int(s[ind:ind+2]) in valid:
                ans+=num_decode_ways(ind+2)
            ans+=num_decode_ways(ind+1)
            memo[ind] = ans

            return ans

        return num_decode_ways(0)

      Time Complexity - O(N)
Space Complexity - O(N)+N stack space

BF Without Memorization - O(2^N)


#==================== Memorization Approach ===============

        dp = [0]*(n+1)

        dp[n] = 1

        for ind in range(n-1,-1,-1):
            if int(s[ind]) == 0:
                continue
            cnt = dp[ind+1]
            if ind+2<=n and int(s[ind:ind+2]) in valid:
                cnt+=dp[ind+2]
            dp[ind] = cnt
        
        return dp[0]

  Time Complexity - O(N)
Space Complexity - O(N)

#=========== Bottom up Aproach ============

    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)

        dp[0] = 1  # Base case: empty prefix
        dp[1] = 1 if s[0] != '0' else 0

        for i in range(2, n + 1):
            # Single digit decode
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]

            # Two digit decode
            two_digit = int(s[i - 2:i])
            if 10 <= two_digit <= 26:
                dp[i] += dp[i - 2]

        return dp[n]

Time Complexity - O(N)
Space Complexity - O(N)

#============= Space optimization ===========
        
      if s[0] == '0':
            return 0

        prev2 = 1  # dp[0]
        prev1 = 1  # dp[1]

        for i in range(2, len(s) + 1):
            current = 0

            # Single digit decode
            if s[i - 1] != '0':
                current += prev1

            # Two digit decode
            two_digit = int(s[i - 2:i])
            if 10 <= two_digit <= 26:
                current += prev2

            prev2 = prev1
            prev1 = current

        return prev1

Time Complexity - O(N)
Space Complexity - O(1)

