class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum=0
        maxSum=nums[0]
        for i in range(len(nums)):
            curSum=max(curSum, 0)
            curSum +=nums[i]
            maxSum = max(curSum, maxSum)
        return maxSum
        