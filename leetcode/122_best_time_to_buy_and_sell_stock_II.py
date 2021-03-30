# 122. Best Time to Buy and Sell Stock II: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # e.g. [7,1,5,3,6,4]
        #       ^ ^
        # Keep two pointers: buy and sell
        # one variable to keep track of global profit
        # initially point at the first number
        # advance sell to point to the next
        # If sell < current price:
        #    consider local profit and add to global
        #    reset local profit
        #    reset sell, buy
        # else:
        #    advance the sell pointer
        if not prices:
            return 0

        globalProfit = 0
        buy,sell = prices[0], prices[0]

        for i in range(1, len(prices)):
            if sell < prices[i]:
                # Sell
                globalProfit += sell - buy
                # update pointers
                buy = prices[i]
            sell = prices[i]


        globalProfit += sell - buy

        return globalProfit

