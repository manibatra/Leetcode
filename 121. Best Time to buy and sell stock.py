class Solution:
	def maxProfit(self, prices):
		if len(prices) < 1:
			return 0
		buy = [0] * len(prices)
		sell = [-1] * len(prices)
		buy[0] = prices[0]
		sell[0] = 0
		for i in range(1, len(prices)):
			buy[i] = min(prices[i], buy[i - 1])
			sell[i] = max(sell[i - 1], prices[i] - buy[i - 1])
			
		return sell[-1]
