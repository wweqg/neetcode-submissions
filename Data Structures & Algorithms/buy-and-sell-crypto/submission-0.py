class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0
        minP = prices[0]
        res = -1

        for i in range(1, n, 1):
            tmp = prices[i] - minP
            res = max(res, tmp)
            minP = min(minP, prices[i])
        
        return max(0, res)