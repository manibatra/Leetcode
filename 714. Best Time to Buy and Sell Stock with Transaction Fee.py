class Solution:
	def maxProfit(self, prices, fee):
		buy = [0] * len(prices)
		sell = [0] * len(prices)
		
		buy[0] = - prices[0] - fee
		sell[0] = 0
		
		for i in range(1, len(prices)):
			buy[i] = max(sell[i - 1] - prices[i] - fee, buy[i - 1])
			sell[i] = max(prices[i] + buy[i - 1], sell[i - 1])
			
		return sell[-1]
		
