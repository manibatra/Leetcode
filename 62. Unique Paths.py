class Solution:
	def uniquePaths(self, m, n):
		if m < 1 or n < 1:
			return 0
		if m == 1 and n == 1:
			return 0
		dp = [[0 for j in range(n)] for i in range(m)]
		return self.countWays(m - 1, n - 1, dp)
	
	def countWays(self, i, j, dp):
		if i == 0:
			return 1
		if j == 0:
			return 1
		if dp[i][j] != 0:
			return dp[i][j]
		dp[i][j] = self.countWays(i - 1, j, dp) + self.countWays(i, j - 1, dp)
		return dp[i][j]
