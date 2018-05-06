class Solution:
	def maxIncreaseKeepingSkyline(self, grid):
		top = []
		left = []
		for i in range(len(grid)):
			left.append(max(grid[i]))
		for i in range(len(grid[0])):
			column = []
			for j in range(len(grid)):
				column.append(grid[j][i])
			top.append(max(column))
		total_sum = 0
		for i in range(len(grid)):
			for j in range(len(grid[0])):
				total_sum += min(top[i], left[j]) - grid[i][j]
				
		return total_sum
