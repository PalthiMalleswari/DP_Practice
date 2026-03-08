# Problem - https://leetcode.com/problems/word-break/

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        n = len(s)
        
        ans_mapp = {}

        def segment_s(rem_str):

            if not rem_str:
                ans_mapp[rem_str] = True
                return ans_mapp[rem_str]
            
            if rem_str in ans_mapp:
                return ans_mapp[rem_str]
            
            for word in wordDict:

                l = min(len(word),len(rem_str))
                
                if word[:l+1]==rem_str[:l]:
                    
                    if segment_s(rem_str[l:]):
                       
                        return True
            
            ans_mapp[rem_str] = False

            return ans_mapp[rem_str]
        
        return segment_s(s)


"""
# ======= Time Complexity  ===========
State -> rem_Str = (leetcode)
no.of possible states for a sting n is n+1 ~ n (leetcode,eetcode,etcode,tcode,code,ode,de,e,"")
Work Done for Each state is - loop over wordict at worst (len = M) and String Comparision inside at worst (n)
so total work done per state is M*n

So,Total Time Complexity -> n(no.of States)*(M*n) Work Done for each state => M*n*2 => M*n^2

# ======= Space Complexity ===========
Space Complexity -> Total no.of unique states (n)+ Recursive Stack Space At worst case(n)
Final Space Compelxity => n+n => 2n => ~n
"""
