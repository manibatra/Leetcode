class Solution:
	def minPathSum(self, grid):
		if len(grid) == 1 and len(grid[0]) == 1:
			return grid[0][0]
		dp = [[-1 for j in range(len(grid[0]))] for i in range(len(grid))]
		return self.minPath(grid, len(grid) - 1, len(grid[0]) - 1, dp)
		
	def minPath(self, grid, i, j, dp):
		if i == 0:
			dp[i][j] = sum(grid[0][column] for column in range(j + 1))
			return dp[i][j]
		if j == 0:
			dp[i][j] = sum(grid[row][0] for row in range(i + 1))
			return dp[i][j]
		if dp[i][j] != -1:
			return dp[i][j]
			
		dp[i][j] = min(grid[i][j] + self.minPath(grid, i - 1, j, dp), 
		grid[i][j] + self.minPath(grid, i, j - 1, dp))
		return dp[i][j]
