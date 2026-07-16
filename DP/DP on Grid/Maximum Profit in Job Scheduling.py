#Problem - https://leetcode.com/problems/maximum-profit-in-job-scheduling/description/

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        
        jobs = []
        for s,e,p in zip(startTime,endTime,profit):
            jobs.append((s,e,p))
        
        jobs.sort(key=lambda ele:ele[1])
        n = len(jobs)
        dp = [0]*n
        dp[0] = jobs[0][2]
        ans = 0

        for i in range(1,n):
            for j in range(i):
                if jobs[j][1] <= jobs[i][0]:

                    dp[i] = max(dp[i],dp[j])

            dp[i] += jobs[i][2]    
            ans = max(ans,dp[i])
        return ans

Time Complexity - O(N*N)
Space Complexity - O(N)

  #===============================================
        jobs.sort(key=lambda x:x[1])
        ends = [j[1] for j in jobs]
        dp2 = [0]*n
        ans2 = 0

        for i in range(n):
            st1,prf1 = jobs[i][0],jobs[i][2]
            take = prf1

            prev = bisect_right(ends,st1)-1
            if prev !=-1:
                take += dp[prev]

            dont = dp[i-1] if i>0 else 0
            
            dp[i] = max(take,dont)
            ans2 = max(ans2,dp[i])

        return ans2

Time Complexity - O(N*logN)
Space Complexity - O(N)
