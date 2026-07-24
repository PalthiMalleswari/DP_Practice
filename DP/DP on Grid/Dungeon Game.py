#Problem - https://leetcode.com/problems/dungeon-game/description/
#Refer Solution -  https://leetcode.com/problems/dungeon-game/solutions/745340/post-dedicated-to-beginners-of-dp-or-hav-whjg/

# state needs to be - Minimum health required before entering cell (i,j) so that you can safely reach the princess.
#============== Memorization Approach =================

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        
        m = len(dungeon)
        n =  len(dungeon[0])
        memo = {}

        def func(r,c):
            
            if r>=m or c>=n:
                return float('inf')

            if r==m-1 and c == n-1:
                return -dungeon[r][c]+1 if dungeon[r][c] <=0 else 1 
            
            if (r,c) in memo:
                return memo[(r,c)]

            down =func(r+1,c)
            right = func(r,c+1)

            min_req = min(down,right) - dungeon[r][c]
            memo[(r,c)] = 1 if min_req <=0 else min_req
            return memo[(r,c)]
            
        ans = func(0,0)
        return ans

Time Complexity - O(M*N)
Space Complexity - O(M*N)+stack space
