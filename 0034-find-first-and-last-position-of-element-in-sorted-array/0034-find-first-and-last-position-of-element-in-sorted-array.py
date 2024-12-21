class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l=0
        r=len(nums)-1
        l1=0
        r1=len(nums)-1
        a=-1
        b=-1
        while l<=r:
            m=l+(r-l)//2
            if nums[m]==target:
                b=m
                l=m+1
            elif nums[m]>target:
                r=m-1
            else:
                l=m+1
        while l1<=r1:
            m1=l1+(r1-l1)//2
            if nums[m1]==target:
                a=m1
                r1=m1 - 1
            elif nums[m1]>target:
                r1=m1-1
            else:
                l1=m1+1
        return [a,b]