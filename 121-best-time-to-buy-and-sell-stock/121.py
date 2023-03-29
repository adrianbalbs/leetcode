class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, j = 0, 1
        maxTotal = 0
        while j < len(prices):
            if prices[i] < prices[j]:
                profit = prices[j] - prices[i]
                maxTotal = max(maxTotal, profit)
            else:
                i = j
            j += 1
        return maxTotal
