# https://leetcode.com/problems/sort-an-array/description/

# =================== Intial Approach =================

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        n = len(nums)

        def merge_sort(st,end):
            mid = (st+end)//2

            if st<end:
                merge_sort(st,mid)
                merge_sort(mid+1,end)
                merge(st,mid,end)
        
        def merge(st,mid,end):

            p1,p2 = st,mid+1
           
            res = []

            while p1<=mid and p2 <= end:
                if nums[p1] <= nums[p2]:
                    res.append(nums[p1])
                    p1+=1

                elif nums[p1] > nums[p2]:
                    res.append(nums[p2]) 
                    p2 += 1

            while p1<=mid:
                res.append(nums[p1])
                p1+=1

            while p2<=end:
                res.append(nums[p2])
                p2 += 1

            nums[st:end+1] = res
               
        merge_sort(0,n-1)
        return nums

  Time Complexity - For a Given N, No.of Levels = logn base 2, Ex:N=8(Level-0 no.of elemens=8(1),L1=4(2),L2=2(4),L3=1(8)) totals levels = 3 log8 base 2
  Each level no.of elements gets divided by half. Work done for each level is N at level 3,work done for 8 single element is 1 Total = 8, At L2 work done for 4 elements is 8.
    
  Time Complexity = No.of Levels * Work Done For Each Level => logn*N => NlogN
                 
  Space Compelxity = N for res + logn for recursion Space = N                                                     
