class Solution:
	def knightProbability(self, N, K, r, c):
		dp = [[[0 for k in range(K + 1)] for j in range(N)] for i in range(N)]
		return self.findPaths(N, K, r, c, 0, dp)/(8**K)

		
	def findPaths(self, N, K, r, c, steps, dp):
		if r >= N or c >= N:
			return 0
		if r < 0 or c < 0:
			return 0
		if steps != 0 and dp[r][c][steps - 1] != 0:
			return dp[r][c][steps - 1]
		if steps == K:
			return 1
		
		x = [1, 2]
		y = [1, -1]
		for i in x:
			for j in x:
				for k in y:
					if i != j:
						dp[r][c][steps - 1] += self.findPaths(N, K, r + i * k, c + j * k, 
						steps + 1, dp)
						dp[r][c][steps - 1] += self.findPaths(N, K, r + i * k, c + j * k * -1, 
						steps + 1, dp)
					
		return dp[r][c][steps - 1]
