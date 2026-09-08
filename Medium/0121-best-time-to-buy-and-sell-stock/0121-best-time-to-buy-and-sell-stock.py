class Solution(object):
    def maxProfit(self, prices):
        min_price = float("inf")
        n = len(prices)
        max_profit = 0
        for i in range(0, n):
            min_price = min(min_price, prices[i])
            max_profit = max(max_profit, prices[i]-min_price)

        return max_profit
            
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna