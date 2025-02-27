class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLength=1000000
        n=len(nums)
        r, l=0, 0
        curSum = 0
        while r<n:
            curSum += nums[r]
            while curSum >= target:
                curSum -= nums[l]
                minLength = min(minLength, r-l+1)
                l+=1
            r+=1
        return minLength if minLength < 1000000 else 0


            

        