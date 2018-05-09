class Solution:
	max_profit = 0
	mem = {}
	prices = []
	def maxProfit(self, prices):
		if len(prices) < 2:
			return 0
		self.mem = {}
		self.prices = prices
		return self.maximiseProfit(prices, 0, 0)
		
		
		
	def maximiseProfit(self, prices, i, num):
		if i >= len(prices):
			return 0
		if i == len(prices) - 1:
			if num == 1:
				return prices[i]
			else:
				return 0
		if (i, num) in self.mem:
			return self.mem[(i, num)]
			
		if num == 0:
			self.mem[(i, num)] = max(-prices[i] + self.maximiseProfit(prices, i + 1, 1),
			self.maximiseProfit(prices, i + 1, 0))
		else:
			self.mem[(i, num)] = max(prices[i] + self.maximiseProfit(prices, i + 2, 0),
			self.maximiseProfit(prices, i + 1, 1))
		
		return self.mem[(i, num)]			
