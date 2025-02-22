class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        l=0
        r=1
        a=0
        for i in range(len(nums)//2):
            a += min([nums[l],nums[r]])
            r +=2
            l +=2
        return a
            
        