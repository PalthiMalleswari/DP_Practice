#Problem - https://leetcode.com/problems/remove-boxes/description/

"""
Maximum score for interval

[l,r]

assuming there are already

k boxes equal to boxes[l]

attached to the left.

dp(l,r,k) = max(
    (k+1)^2 + dp(l+1,r,0),

    max over every m where boxes[m]==boxes[l]:
        dp(l+1,m-1,0) + dp(m,r,k+1)
)

"""
#============= Tracedown the problem with an example ===========

class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        
        n = len(boxes)
        memo = {}

        def dp(l,r,k):
            if l>r:
                 return 0

            while l+1 <=r and boxes[l] == boxes[l+1]:
                l+=1
                k+=1            
            
            if (l,r,k) in memo:
                return memo[(l,r,k)] 
                
            
            ans = (k+1)*(k+1) + dp(l+1,r,0)

            for m in range(l+1,r+1):
                if boxes[l]==boxes[m]:
                    ans = max(ans,dp(m,r,k+1) + dp(l+1,m-1,0))
            memo[(l,r,k)] = ans
            return memo[(l,r,k)]

        return dp(0,n-1,0)
      
Space Complexity - O(N*3) states are possible

Time Complexity - For every state we need to scan the entire array in worst case to compute the best points. So - O(N*4)
