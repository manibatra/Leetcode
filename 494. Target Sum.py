class Solution:
	def findTargetSumWays(self, nums, S):
	 dp = [[-1 for j in range(2000)] for i in range(len(nums))]
	 
	 return self.maxWays(nums, S, 0, 0, dp)
	 
	 
	def maxWays(self, nums, S, i, sum, dp):
		if i == len(nums):
			if sum == S:
				return 1
			else:
				return 0
				
		if dp[i][sum + 1000] != -1:
			return dp[i][sum + 1000]
			
		
		add = self.maxWays(nums, S, i + 1, sum + nums[i], dp)
		subtract = self.maxWays(nums, S, i + 1, sum - nums[i], dp)
		
		dp[i][sum + 1000] = add + subtract
		
		return dp[i][sum + 1000]
