class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j=0
        n=len(nums)
        for i in range(n):
            if val != nums[i]:
                nums[j]=nums[i]
                j+=1
        return j