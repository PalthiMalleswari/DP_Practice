#Problem - https://leetcode.com/problems/pascals-triangle/

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1],[1,1]]
        
        ans = [[1],[1,1]]

        for i in range(2,numRows):
            tmp = [1]*(i+1)
            for j in range(1,i):
                tmp[j]=ans[i-1][j-1]+ans[i-1][j]
            ans.append(tmp)
        return ans

Time Complexity - O(N*N)
Space Complexity - O(N*N)

#DP can be applicable here because each row's value only depends on it's previous row
# Optimization - Math Logic with combinations !
    
