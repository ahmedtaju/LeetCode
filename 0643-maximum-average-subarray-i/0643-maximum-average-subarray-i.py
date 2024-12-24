class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        subArray = [nums[i] for i in range(k)]
        new_sum = sum(subArray)
        max_sum = new_sum
        left = 1
        right = k
        if k == 1:
            return max(nums)
        while right < len(nums):
            new_sum = new_sum - nums[left-1] + nums[right]
            print(new_sum)
            if new_sum > max_sum:
                max_sum = new_sum
            right += 1
            left += 1
        return max_sum/k
            