#Problem - https://leetcode.com/problems/cherry-pickup-ii/


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        
        m,n = len(grid),len(grid[0])
        memo = {}

        def pick_max_chery(r1,c1,r2,c2):

            if not (
                0<=c1<n and 0<=c2<n and r1<m and r2<m
            ):
                return float('-inf')

            if r1==m-1 or r2 ==m-1:
                if c1 == c2:
                    return grid[r1][c1]
                return grid[r1][c1]+grid[r2][c2]

            if (r1,c1,r2,c2) in memo:
                return memo[(r1,c1,r2,c2)]
            
            cherry = 0
            
            if r1==r2 and c1==c2:
                cherry += grid[r1][c1]
            
            else:
                cherry = grid[r1][c1]+grid[r2][c2]

            best = float('-inf')
            for dir1 in [-1,0,1]:
                for dir2 in [-1,0,1]:
                    best = max(best,pick_max_chery(r1+1,c1+dir1,r2+1,c2+dir2))

            memo[(r1,c1,r2,c2)] = cherry+best
            return memo[(r1,c1,r2,c2)]

        return pick_max_chery(0,0,0,n-1)

# TimeComplexity - O(M*N*M*N)
# Space Complxity - O(M*N*M*N) +O(M)

#=================== State Reduction ====================

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        
        m,n = len(grid),len(grid[0])
        memo = {}

        def pick_max_chery(r1,c1,c2):

            if not (
                0<=c1<n and 0<=c2<n and r1<m
            ):
                return float('-inf')

            if r1==m-1:
                if c1 == c2:
                    return grid[r1][c1]
                return grid[r1][c1]+grid[r1][c2]

            if (r1,c1,c2) in memo:
                return memo[(r1,c1,c2)]
            
            cherry = 0
            
            if c1==c2:
                cherry += grid[r1][c1]
            
            else:
                cherry = grid[r1][c1]+grid[r1][c2]

            best = float('-inf')
            for dir1 in [-1,0,1]:
                for dir2 in [-1,0,1]:
                    best = max(best,pick_max_chery(r1+1,c1+dir1,c2+dir2))

            memo[(r1,c1,c2)] = cherry+best
            return memo[(r1,c1,c2)]

        return pick_max_chery(0,0,n-1)
            

      Time Complexity - O(M*N*N)
      Space Complexity - O(M*N*N) + stack space (m)
