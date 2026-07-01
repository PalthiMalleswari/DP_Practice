#Problem - https://leetcode.com/problems/triangle/description/

#Idea : To avoid unnessacary edge cases we should traversing the triangle in a backward direction

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        n = len(triangle[-1])

        for i in range(n-2,-1,-1):
      
            for j in range(len(triangle[i])):
                
                below = triangle[i+1][j]
                bel_right = triangle[i+1][j+1]

                triangle[i][j] += min(below,bel_right)

        return triangle[0][0]


Time Complexity - O(N*N)
Space Complexity - O(1)
