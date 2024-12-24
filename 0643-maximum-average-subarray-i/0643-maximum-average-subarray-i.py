class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        new_sum = sum(nums[:k])
        max_sum = new_sum
        n = len(nums)
        left = 1
        right = k
        if k == 1:
            return max(nums)
        while right < n:
            new_sum = new_sum - nums[left-1] + nums[right]
            if new_sum > max_sum:
                max_sum = new_sum
            right += 1
            left += 1
        return max_sum/k
            