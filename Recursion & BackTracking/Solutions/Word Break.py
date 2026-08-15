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



class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        n = len(s)
        memo = {}

        def can_segment(ind):
            
            if ind>=n:
                return True
            
            if ind in memo:
                return memo[ind]

            for word in wordDict:
                
                wl = len(word)
                if ind+wl-1 < n:
                    
                    i = 0
                    
                    while i<wl and s[ind+i]==word[i]:
                        i+=1
                    
                    if i<wl:
                        continue
                    
                    if can_segment(ind+i):
                        memo[ind] = True
                        return True

            memo[ind] = False
            return False

        # return can_segment(0)

        dp = [False]*(n+1)

        dp[0] = True

        for i in range(1,n+1):

            for word in wordDict:

                wl = len(word)

                if i-wl>=0:

                    st = i-wl
                    j = 0
                    
                    while j<wl and s[st+j]==word[j]:
                        j+=1
                    
                    if j<wl:
                        continue
                    # print(j,wl,word,i)
                    dp[i] = dp[i] or dp[i-wl]
        # print(dp)
        return dp[n]


