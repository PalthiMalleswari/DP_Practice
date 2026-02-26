# Problem - https://leetcode.com/problems/palindrome-partitioning/description/

At index start:
Try all possible substring endings end from start index
If s[start:end+1] is palindrome
Add it
Recurse from end+1

# ============ Exponential Approach ===============

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        n = len(s)
        ans = []

        def do_partitions(ind,prtion):

            if ind == n:
                ans.append(prtion[:])
                return
            
            for end in range(ind,n):

                substring = s[ind:end+1]

                if substring[:]==substring[::-1]:

                    prtion.append(substring)

                    do_partitions(end+1,prtion)

                    prtion.pop()
    
        do_partitions(0,[])
        return ans

Time Complexity -> O(N*2^N) #N for Pallindrom Check +  Each Element has two states partion or not 
Space Complexity -> O(N+N)  # Path + Recursive Stack Space
