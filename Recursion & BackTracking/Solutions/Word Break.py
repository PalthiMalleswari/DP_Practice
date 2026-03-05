# Problem - https://leetcode.com/problems/word-break/description/

# ======================== Approach =============================

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

# Time Complexity - 
# Space Complexity -  
