class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        _min = prices[0]
        _max = 0
        for i in prices:
            profit = i - _min
            _max = max(_max, profit)
            _min = min(i, _min)
        return _max
