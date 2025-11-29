"""
You are given an integer array nums of 2 * n integers. You need to partition nums into two arrays of length n to minimize the absolute difference of the sums of the arrays.
To partition nums, put each element of nums into one of the two arrays.
Return the minimum possible absolute difference.

Input: nums = [3,9,7,3]
Output: 2
Explanation: One optimal partition is: [3,9] and [7,3].
The absolute difference between the sums of the arrays is abs((3 + 9) - (7 + 3)) = 2.

"""

"""
IDEA :
P1,P2 are subsets whose corresponding sums are s1 and s2
We neeed min(|s1 - s2|) 
Tota Sum(TS) = s1+s2
s2 = TS-s1

if we know all possible subset sum for P1, we can compute it's corresponding s2, and we return min among them
"""


class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        
        totalSum = sum(nums)
        n = len(nums)

        dp = [[-1 for j in range(totalSum+1)] for i in range(n)]
        
        def cal_subset_sum(ind,target):

            if target == 0:
                dp[ind][target] = True
                return True

            if ind == 0:
                # res = 
                dp[ind][target] = (target == nums[ind])
                return dp[ind][target]

            if dp[ind][target] != -1:
                return dp[ind][target]

            bool_not = cal_subset_sum(ind-1,target)
            bool_take = False

            if nums[ind]<=target:

                bool_take = cal_subset_sum(ind-1,target-nums[ind])

            dp[ind][target] = bool_take or bool_not

            return dp[ind][target]
          
        # Find all Possible Subset Sum for Partition 1 
        for i in range(totalSum+1):

            cal_subset_sum(n-1,i)

        print(dp)
        min_ans = float('inf')

        for s1 in range(totalSum+1):
          
            # If S1 is Valid Sum
            if dp[n-1][s1]:

                s2 = totalSum-s1 
                min_ans = min(min_ans,abs(s2-s1))
        return min_ans
      
#### If Input Array Has Negitive Elements, we can't depresent it in a array

## Meet -In- Middle Technique
n = len(nums)
N = n // 2
total_sum = sum(nums)

left = [[] for _ in range(N + 1)]
right = [[] for _ in range(N + 1)]

for mask in range(1 << N):
    sz = 0
    l = 0
    r = 0
    for i in range(N):
        if mask & (1 << i):
            sz += 1
            l += nums[i]
            r += nums[i + N]
    left[sz].append(l)
    right[sz].append(r)

for arr in right:
    arr.sort()

res = min(abs(total_sum - 2 * left[N][0]), abs(total_sum - 2 * right[N][0]))

for sz in range(1, N):
    for a in left[sz]:
        target = (total_sum - 2 * a) // 2
        rsz = N - sz
        arr = right[rsz]

        idx = bisect_left(arr, target)

       
        if idx < len(arr):
            res = min(res, abs(total_sum - 2 * (a + arr[idx])))

      
        if idx > 0:
            res = min(res, abs(total_sum - 2 * (a + arr[idx - 1])))

return res
