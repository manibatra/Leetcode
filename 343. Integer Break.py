class Solution:
	def integerBreak(self, n):
		ans = [0] * max(5, (n + 1))
		ans[1] = 1
		for i in range(2, n + 1):
			for j in range(int(i/2), i + 1):
				if j < 4:
					ans[i] = max(ans[i], j * (i - j))
				else:
					ans[i] = max(ans[i], ans[j] * ( i - j))
		
		return ans[n]
