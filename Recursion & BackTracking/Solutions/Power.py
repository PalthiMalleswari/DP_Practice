# Problem - https://leetcode.com/problems/count-good-numbers/

# ==============  Approach 1 ===========

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        
        Mod = 10**9+7
        s = 1
        for i in range(n):

            if i%2 == 0:
                s = (s*5)%Mod
            else:
                s = (s*4)%Mod
        return s%Mod


# ==============  Approach 2 ===========

      if n%2 == 0:

          evn,odd = n//2,n//2
      
      else:

          evn,odd = n//2+1,n//2
      
      five = pow(5,evn)%Mod
      four = pow(4,odd)%Mod
      return (five*four)%Mod



Time Complexity - O(N) power function
Space Complexity - O(1)

# ============== Optiizzed Approach (Binart Representation) ==================

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        
        Mod = 10**9+7

        odd = n//2
        even = n-odd
        ans = self.power(4,odd,Mod)%Mod*self.power(5,even,Mod)%Mod
        return ans%Mod
       
    
    def power(self,x,n,Mod):

        res = 1
        while n > 0:
            if n&1:
                res=(res*x)%Mod
            x=(x*x)%Mod
            n>>=1
        return res

Time Complexity - O(log N)
Space Complexity - O(1)

# ============== If n is negative and x is float ====================

class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        ans = self.power(x,abs(n))
        if n<0:
            ans = 1/float(ans) 
        return ans
    
    def power(self,x,n):

        res = 1

        while n>0:

            if n&1:
                res*=x
        
            x = float(x*x)
            n >>= 1
        return float(res)
    
        

