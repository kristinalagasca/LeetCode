"""
Given a list of integers prices representing the stock prices of a company in chronological order, return the maximum profit you could have made from buying and selling that stock any number of times.

You must buy before you can sell it. But you are not required to buy or sell the stock.
"""

class Solution:
    def solve(self, prices):
        return sum(max(0,prices[i]-prices[i-1]) for i in range(1,len(prices)))
