# Problem - https://leetcode.com/problems/delete-and-earn/

# ===================== Top Down Approach ========================

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        
        n = len(nums)
        nums.sort()
        memo = {}

        def find_max_points(ind):

            if ind >=n:
                return 0
            
            if ind in memo:
                return memo[ind]

            i = ind+1
            cur_pnt = nums[ind]

            while i<n and nums[ind]==nums[i]:
                cur_pnt += nums[i]
                i+=1

            while i<n and nums[i]==nums[ind]+1:
                i+=1
            
            memo[ind] = max(cur_pnt+find_max_points(i),find_max_points(ind+1))
            return memo[ind]
            
        return find_max_points(0)

  Time Complexity - O(N)+Nlogn
  Space Complexity - O(N+N) Recursive Call Stack+Memo Hashmap

#================== Bottom up ==========================


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
    
        buckets = [0]*10001
        for num in nums:
            buckets[num] += num
        dp = [0]*10001

        dp[0],dp[1] = buckets[0],buckets[1]
        for i in range(2,len(buckets)):
            dp[i]= max(buckets[i]+dp[i-2],dp[i-1])
        return dp[10000]

Time Complexity - O(10001)
Space Complexity - O(10001+10001)
