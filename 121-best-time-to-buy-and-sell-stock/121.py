class Solution:
    def maxProfit(self, prices: List[int]) -> int:
            i,j = 0,1
            maxTotal = 0
            while j != len(prices):
                if prices[i] > prices[j]:
                    i += 1
                    j += 1
                else:
                    maxTotal = max(maxTotal, prices[j] - prices[i])
                    j += 1
            return maxTotal

