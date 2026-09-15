class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        mx = 0
        prev = prices[0]
        for price in prices:
            if price - prev > mx:
                mx = price - prev
            if price < prev:
                prev = price
        return mx