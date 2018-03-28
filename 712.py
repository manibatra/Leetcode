class Solution:
	def minimumDeleteSum(self, s1, s2):
		dp = [[0 for j in range(len(s2) + 1)] for i in range(len(s1) + 1)]
		
		for i in range(1, len(s1) + 1):
			for j in range(1, len(s2) + 1):
				if s1[i-1] == s2[j-1]:
					dp[i][j] = dp[i-1][j-1] + 2 * ord(s1[i-1])
				else:
					dp[i][j] = max(dp[i-1][j], dp[i][j-1])
							
		
										
		s1_ascii = sum(ord(c) for c in s1)
		s2_ascii = sum(ord(c) for c in s2)
		return (s1_ascii + s2_ascii - dp[len(s1)][len(s2)])
