class Solution:
	def climbStairs(self, n):
		if n <= 2:
			return n
		dp = [-1] * (n + 1)
		return self.totalWays(n, dp)
		
	def totalWays(self, n, dp):
		if n == 0:
			return 1
		if n < 0:
			return 0
		if dp[n] != -1:
			return dp[n]
		dp[n] = self.totalWays(n - 1, dp) + self.totalWays(n - 2, dp)
		return dp[n]
