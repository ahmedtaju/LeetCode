class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap={}
        for i, value in enumerate(nums):
            diff=target-value
            if diff in hashMap:
                return [i, hashMap[diff]]
            hashMap[value]=i