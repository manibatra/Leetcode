class Solution:
	def countNumbersWithUniqueDigits(self, n):
		ans = [0] * (n + 1)
		ans[0] = 1
		
		
		for i in range(1, n + 1):
			ans[i] = ans[i - 1] + self.unique(i)
			
		return ans[n]
		
		
	def unique(self, digits):
		product = 9
		factor = 9
		for i in range(1, digits):
			product *= factor
			factor -= 1
		return product
				
