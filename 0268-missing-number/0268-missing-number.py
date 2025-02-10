class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i=0
        n=len(nums)
        while i<n:
            if nums[i]<n and nums[i] != i:
                nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
            else:
                i += 1
        for i in range(n):
            if i != nums[i]:
                return i
        return n
        