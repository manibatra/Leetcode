class Solution:
	def longestPalindromSubseq(self, s):
		if len(s) <= 1:
			return len(s)
		if s == s[::-1]:
			return len(s)
		rev_s = s[::-1]
		dp = [[0 for j in range(len(s) + 1)] for i in range(len(s) + 1)]
		i = 1
		j = 1
		while i < len(s) + 1:
			j = 1
			while j < len(s) + 1:
				if s[i - 1] == rev_s[j - 1]:
					dp[i][j] = 1 + dp[i - 1][j - 1]
					j += 1
				else:
					dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
					j += 1
			i += 1
		print(dp)
		return dp[len(s)][len(s)]
		#return self.longestSub(s, s[::-1], len(s) - 1, len(s) - 1, dp)
		
	def longestSub(self, a, b, i, j, dp):
		#print(i, j)
		if i < 0 or j < 0:
			return 0
		if dp[i][j] != 0:
			return dp[i][j]
		if a[i] == b[j]:
			dp[i][j] = max(dp[i][j], 1 + self.longestSub(a, b, i - 1, j - 1, dp))
		else:
			dp[i][j] = max(dp[i][j], max(self.longestSub(a, b, i - 1, j, dp), self.longestSub(a, b, i, j - 1, dp)))
		
		print(dp)
		return dp[i][j]
		
