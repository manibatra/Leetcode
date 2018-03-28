import math
class Solution:
	def countBits(self, num):
		ans = [math.inf] * (num + 1)
		ans[0] = 0

		for i in range(1, num + 1):
			j = 1
			while j <= i:
				if j == i:
					ans[i] = 1
				else:
					ans[i] = min(ans[i], ans[j] + ans[i - j])
				j *= 2
		return ans

