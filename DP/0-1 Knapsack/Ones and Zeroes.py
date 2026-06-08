#Problem - https://leetcode.com/problems/ones-and-zeroes/

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        
        le = len(strs)
        dp = {}
  
        def get_max_len(ind,z,o):

            if ind<0:
                return 0
            if (ind,z,o) in dp:
                return dp[(ind,z,o)]
            
            take = 0
            if z-strs[ind].count('0')>=0 and o-strs[ind].count('1')>=0:
                take = get_max_len(ind-1,z-strs[ind].count('0'),o-strs[ind].count('1'))+1
            dont = get_max_len(ind-1,z,o)
            
            dp[(ind,z,o)] = max(take,dont)
            return dp[(ind,z,o)]

        return get_max_len(le-1,m,n)

#Time Complexity - O(Len(Strs)*M*N)
#Space Complexity - O(len(strs)*m*n)
