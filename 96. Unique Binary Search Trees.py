class Solution:
	def numTrees(self, n):
		if n < 3:
			return n
			
		dp = [0] * (n + 1)
		dp[0] = 1
		dp[1] = 1
		dp[2] = 2
		
		for i in range(3, n + 1):
			for j in range(1, i + 1):
				#print(j - 1, n - j)
				dp[i] += (dp[j - 1] * dp[i - j])
		#print(dp)
		return dp[-1]	
