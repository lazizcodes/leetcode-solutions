class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res, dp, n = 0, 0, len(prices)
        for i in range(n - 1):
            q = prices[i + 1] - prices[i]
            dp = max(dp + q, q)
            res = max(res, dp)
        return res