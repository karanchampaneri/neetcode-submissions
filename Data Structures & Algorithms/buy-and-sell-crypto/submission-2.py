class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        bestBuy = prices[0] 
        profit = 0

        for i in range(len(prices)-1):

            if prices[i+1] <= bestBuy: #next day better?
                bestBuy = prices[i+1]

            if prices[i+1] - bestBuy >= profit:
                profit = prices[i+1] - bestBuy

        return profit
                


                