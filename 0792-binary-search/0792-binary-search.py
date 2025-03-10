class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1
        while left<=right:
            middle=(right+left)//2
            if target==nums[middle]:
                return middle
            elif target>nums[middle]:
                left=middle+1
            elif target<nums[middle]:
                right=middle-1
        return -1