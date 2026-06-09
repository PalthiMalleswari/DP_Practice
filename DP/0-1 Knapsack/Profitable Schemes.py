# Problem - https://leetcode.com/problems/profitable-schemes/description/

#Recursive Version with (MLE for test case 40/45)

class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        
        nn = len(group)
        dp = {}

        def no_of_ways(ind,prf,rem_n):

            if ind==-1:
                if prf<minProfit:
                    return 0
                else:
                    return 1

            if (ind,prf,rem_n) in dp:
                return dp[(ind,prf,rem_n)]

            dont = no_of_ways(ind-1,prf,rem_n)
            take = 0
            if rem_n>=group[ind]:
                take = no_of_ways(ind-1,prf+profit[ind],rem_n-group[ind])
            dp[(ind,prf,rem_n)] = dont+take
            return dp[(ind,prf,rem_n)]

        return no_of_ways(nn-1,0,n)
      
  Time Complexity - O(len(profits)*minProfit*n)
  Space Complexity - O(len(profits)*minProfit*n)
