class Solution:
	def minSteps(self, n):
		dp = [-1] * (n + 1)
		if n < 2:
			return 0
		dp[1] = 0
		return self.ans(dp, n)
		
	def ans(self, dp, n):
		if dp[n] != -1:
			return dp[n]
		else:
			x = self.findFactor(n)
			dp[n] = self.ans(dp, x) + 1 + (int(n/x) - 1)
		return dp[n]
		
	def findFactor(self, n):
		for i in range(int(n/2), 0, -1):
			if n % i == 0:
				return i
