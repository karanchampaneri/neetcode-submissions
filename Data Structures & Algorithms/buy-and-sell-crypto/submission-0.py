class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # profit = 0

        # for i in range(len(prices)):
        #     for j in range(i+1, len(prices)):
        #         if prices[j] - prices[i] >= profit:
        #             profit = prices[j] - prices[i]
    
        # return profit

        best_buy = prices[0]
        max_profit = 0

        for i in range(len(prices)-1):
            if prices[i+1] <= best_buy:
                best_buy = prices[i+1]
            
            if prices[i+1] - best_buy >= max_profit:

                max_profit = prices[i+1] - best_buy

        return max_profit










            