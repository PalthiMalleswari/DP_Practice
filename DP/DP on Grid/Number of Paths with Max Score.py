#Problem - https://leetcode.com/problems/number-of-paths-with-max-score/description/

#=================== Wrong Ans for 33/34 ===================
class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        
        n = len(board)
        dp = [[[-1,0] for j in range(n)] for _ in range(n)]

        dp[n-1][n-1] = [0,1]
        Mod = 10**9+7
        
        for i in range(n-1,-1,-1):

            for j in range(n-1,-1,-1):

                if (i==n-1 and j==n-1) or board[i][j]=='X':
                    continue
                
                best_score = -1
                ways = 0

                #Three possible ways
                if i+1<n:
                    score,cnt = dp[i+1][j]

                    if score>best_score:
                        best_score = score
                        ways = cnt
                    elif score==best_score and score!=-1:
                        ways = (ways+cnt)%Mod
                if j+1<n:
                    score,cnt = dp[i][j+1]
                    if score>best_score:
                        best_score = score
                        ways = cnt
                    elif score == best_score and score != -1:
                        ways = (ways+cnt)%Mod
                if i+1<n and j+1<n:
                    score,cnt = dp[i+1][j+1]
                    if score>best_score:
                        best_score = score
                        ways = cnt
                    elif score == best_score and score != -1:
                        ways = (ways+cnt)%Mod
                if best_score == -1:
                    continue
                if board[i][j] in 'SE':
                    val = 0
                else:
                    val = int(board[i][j])
                dp[i][j][0] = val+best_score
                dp[i][j][1] = ways%Mod
        # print(dp)
        if dp[0][0][1] == 0:
            return [0,0]
        return [dp[0][0][0],dp[0][0][1]
                

        return [bst_sum,bst_cnt]


#================== Optimal Approach ==========================

class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        
        MOD = 10**9 + 7
        n = len(board)

        next_score = [-1] * (n + 1)
        next_ways = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            # Fresh arrays store the current row.
            curr_score = [-1] * (n + 1)
            curr_ways = [0] * (n + 1)

            for j in range(n - 1, -1, -1):
                cell = board[i][j]

                if cell == 'X':
                    continue

                if cell == 'S':
                    curr_score[j] = 0
                    curr_ways[j] = 1
                    continue

                best = max(
                    next_score[j],
                    curr_score[j + 1],
                    next_score[j + 1]
                )

                if best == -1:
                    continue

                ways = 0

                if next_score[j] == best:
                    ways += next_ways[j]
                if curr_score[j + 1] == best:
                    ways += curr_ways[j + 1]
                if next_score[j + 1] == best:
                    ways += next_ways[j + 1]

                value = 0 if cell == 'E' else int(cell)

                curr_score[j] = best + value
                curr_ways[j] = ways % MOD

            next_score = curr_score
            next_ways = curr_ways

        if next_score[0] == -1:
            return [0, 0]

        return [next_score[0], next_ways[0]]

  Time Complexity - O(N*N)
  Space Complexity - O(N+N)
