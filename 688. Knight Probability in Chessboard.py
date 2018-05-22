class Solution:
	total_paths = 0
	off_board = 0
	dp = []
	def knightProbability(self, N, K, r, c):
		self.total_paths = 0
		self.off_board = 0
		self.dp = [[-1 for j in range(N)] for i in range(N)]
		self.findPaths(N, K, r, c, 0)
		#print(self.total_paths - self.off_board, 8**K)
		return (self.total_paths - self.off_board)/(8**K)
		
	def findPaths(self, N, K, r, c, steps):
		if r >= N or c >= N:
			self.off_board += 1
			self.total_paths += 1
			return
		if r < 0 or c < 0:
			self.off_board += 1
			self.total_paths += 1
			return
		if steps == K:
			self.total_paths += 1
			self.dp[r][c] = (self.off_board, self.total_paths)
			return
		if self.dp[r][c] != -1:
			self.off_board += self.dp[r][c][0]
			self.total_paths += self.dp[r][c][1]
			return 
		x = [1, 2]
		y = [1, -1]
		for i in x:
			for j in x:
				for k in y:
					if i != j:
						self.findPaths(N, K, r + i * k, c + j * k, steps + 1)
						self.findPaths(N, K, r + i * k, c + j * k * -1, steps + 1)
					
		return
