# Problem - https://leetcode.com/problems/last-stone-weight-ii/description/


#Smashing means a series of additions and subtractions for each number


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        n = len(stones)
        dp = {}
        def min_weight(ind,rem_w):
            if ind<0:
                return rem_w
            if (ind,rem_w) in dp:
                return dp[(ind,rem_w)]
            
            neg = min_weight(ind-1,rem_w-stones[ind])
            pos = min_weight(ind-1,rem_w+stones[ind])

            dp[(ind,rem_w)] = min(abs(neg),abs(pos))
            return dp[(ind,rem_w)]

        return min_weight(n-1,0)

Time Complexity - O(N*totalsum)
Space Complexity - O(N*totalsum)

#============== optimal Approach ===================

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        n = len(stones)
        total = sum(stones)
        target = total//2

        dp = [False]*(target+1)
        dp[0] = True

        for num in stones:
            for s in range(target,-1,-1):
                if s>=num:
                    dp[s] = dp[s] or dp[s-num]

        for s in range(target,-1,-1):
            if dp[s]:
                return abs(2*s-total)
        return 0

Time Complexity - O(n*total/2)
Space Complexity - O(total/2)
