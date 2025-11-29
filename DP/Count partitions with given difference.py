"""
Given an array arr of n integers and an integer diff, count the number of ways to partition the array into two subsets S1 and S2 such that:
∣S1−S2∣ = diff and S1 ≥ S2
Where |S1| and |S2| are sum of Subsets S1 and S2 respectively.
Return the result modulo 109 + 7.
Note: A partition means that the union of S1 and S2 is the original array, and no element is left out or used twice — every element of the array belongs to exactly one of the two subsets.

S1 - S2 = diff
:: S1 = diff + S2

S1 + S2 = Ts
diff+S2+S2 = Ts
diff + 2*S2 = Ts
S2 = (Ts-diff)//2

"""

class Solution:
    def countPartitions(self, n, diff, arr):

        MOD = 10**9 + 7
        Ts = sum(arr)

        # Validity checks
        if (Ts - diff) < 0 or (Ts - diff) % 2 != 0:
            return 0

        targetSum = (Ts - diff) // 2

        # DP array initialized with -1 (meaning "not computed")
        dp = [[-1 for _ in range(targetSum + 1)] for _ in range(n)]

        def get_partition_sum(ind, ts):

            # Base case
            if ind == 0:
                if ts == 0 and arr[0] == 0:
                    return 2   # pick or not pick
                if ts == 0:
                    return 1   # do not take arr[0]
                if arr[0] == ts:
                    return 1   # take arr[0]
                return 0

            # Memoized result
            if dp[ind][ts] != -1:
                return dp[ind][ts]

            # Not taking this element
            notTake = get_partition_sum(ind - 1, ts) % MOD

            # Taking this element (if possible)
            take = 0
            if ts >= arr[ind]:
                take = get_partition_sum(ind - 1, ts - arr[ind]) % MOD

            dp[ind][ts] = (take + notTake) % MOD
            return dp[ind][ts]

        return get_partition_sum(n - 1, targetSum) % MOD


Time Complexity : O(N*targeSum)
Space Complexity : O(N*targetSum)

##=======================Tabulation ============================

def countPartitions(n, diff, arr):

    MOD = 10**9 + 7
    Ts = sum(arr)

    # Invalid case
    if (Ts - diff) < 0 or (Ts - diff) % 2 != 0:
        return 0

    targetSum = (Ts - diff) // 2

    # Create dp table
    dp = [[0 for _ in range(targetSum + 1)] for _ in range(n)]

    # Base case for index 0
    if arr[0] == 0:
        dp[0][0] = 2      # pick or not pick
    else:
        dp[0][0] = 1      # only not-pick possible

    if arr[0] != 0 and arr[0] <= targetSum:
        dp[0][arr[0]] = 1

    # Fill DP table
    for i in range(1, n):
        for ts in range(targetSum + 1):

            not_take = dp[i-1][ts] % MOD

            take = 0
            if ts >= arr[i]:
                take = dp[i-1][ts - arr[i]] % MOD

            dp[i][ts] = (take + not_take) % MOD

    return dp[n-1][targetSum] % MOD

##=========================== Space Optimization ==============================

def countPartitions(n, diff, arr):

    MOD = 10**9 + 7
    Ts = sum(arr)

    # Invalid case
    if (Ts - diff) < 0 or (Ts - diff) % 2 != 0:
        return 0

    targetSum = (Ts - diff) // 2

    prev = [0] * (targetSum + 1)

    # Base case (i = 0)
    if arr[0] == 0:
        prev[0] = 2      # pick or not pick
    else:
        prev[0] = 1      # only not pick

    if arr[0] != 0 and arr[0] <= targetSum:
        prev[arr[0]] = 1

    # Build DP
    for i in range(1, n):
        cur = [0] * (targetSum + 1)

        for ts in range(targetSum + 1):

            not_take = prev[ts]

            take = 0
            if ts >= arr[i]:
                take = prev[ts - arr[i]]

            cur[ts] = (take + not_take) % MOD

        prev = cur

    return prev[targetSum] % MOD


