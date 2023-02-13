class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # assume that the minimum selling price of stock is the first item in prices
        _min = prices[0]
        _max = 0  # assume that the maximum profit is 0
        for i in prices:
            profit = i - _min
            _max = max(_max, profit)
            _min = min(i, _min)
        return _max
