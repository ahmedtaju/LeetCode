class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        max_profit = 0
        while right < len(prices):
            cur_sum = prices[right] - prices[left]
            if prices[right] > prices[left]:
                max_profit = max(max_profit, cur_sum)
            else:
                left=right
            right += 1
        return max_profit
        
        