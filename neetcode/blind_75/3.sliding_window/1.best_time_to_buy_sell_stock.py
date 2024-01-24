from typing import List


class Solution:
    """
    https://leetcode.com/problems/best-time-to-buy-and-sell-stock
    """

    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        profit = 0
        max_profit = 0

        while r < len(prices):
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
            else:
                l = r
            r += 1
        return max_profit

        #    def maxProfit(self, prices: List[int]) -> int:
        #        lowest_price = prices[0]
        #        highest_profit = 0
        #
        #        for price in prices:
        #            if (price - lowest_price) > highest_profit:
        #                highest_profit = price - lowest_price
        #            if price < lowest_price:
        #                lowest_price = price
        #
        #        return highest_profit