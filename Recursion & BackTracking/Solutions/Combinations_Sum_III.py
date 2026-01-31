# Problem - https://leetcode.com/problems/combination-sum-iii/description

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        comb = []
        arr = [1,2,3,4,5,6,7,8,9]
        ans = []

        if k>n:
            return ans

        def cal_comb(ind,tar):

            if tar == 0 and len(comb)==k:
                ans.append(comb[:])
            
            for i in range(ind,9):

                if arr[i]<=tar:
                    comb.append(arr[i])
                    cal_comb(i+1,tar-arr[i])
                    comb.pop()
        cal_comb(0,n)
        return ans


Time Complexity - O(2^N)
Space Complexity - O(N+N)
