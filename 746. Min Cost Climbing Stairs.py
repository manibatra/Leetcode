class Solution:
	cost = []
	dp = []
	def minCostClimbingStairs(self, cost):
		cost += [0]
		dp = [0] * len(cost)
		self.cost = cost
		self.dp = dp
		return self.minCost(len(cost) - 1)
		
	def minCost(self, i):
		if i < 0:
			return 0
		if self.dp[i] != 0:
			return self.dp[i]
		self.dp[i] = self.cost[i] + min(self.minCost(i - 1), self.minCost(i - 2))
		return self.dp[i]
