class Solution:
	def longestPalindromeSubseq(self, s):
		if len(s) <= 1:
			return len(s)
		if s == s[::-1]:
			return len(s)
		dp = [[0 for j in range(len(s))] for i in range(len(s))]
		return self.longestSub(s, 0, len(s) - 1, dp)
		
	def longestSub(self, s, i, j, dp):
		#print(i, j)
		if i > j:
			return 0
		if i == j:
			return 1
		if dp[i][j] != 0:
			return dp[i][j]
		if s[i] == s[j]:
			dp[i][j] = max(dp[i][j], 2 + self.longestSub(s, i + 1, j - 1, dp))
		else:
			dp[i][j] = max(dp[i][j], max(self.longestSub(s, i + 1, j, dp), self.longestSub(s,i, j - 1, dp)))
		
		#print(dp)
		return dp[i][j]
		
