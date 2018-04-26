class Solution:
	def maxCoins(self, nums):
		if len(nums) < 1: 
			return 0
		if len(nums) == 1:
			return nums[0]
		if len(nums) == 2:
			return (nums[0] * nums[1]) + max(nums[0], nums[1])
			
		nums = [1] + [x for x in nums if x != 0] + [1]
		dp = [[0 for j in range(len(nums) - 1)] for i in range(len(nums) - 1)]
		return self.maxSum(nums, dp, 1, len(nums) - 2)
		
		
	def maxSum(self, nums, dp, start, end):
		#print(nums, start, end)
		if start > end:
			return 0
		if dp[start][end] != 0:
			return dp[start][end]
		for i in range(start, end + 1):
			dp[start][end] = max(dp[start][end], nums[start - 1] * nums[i] * nums[end + 1] + self.maxSum(nums, dp, start, i - 1) + self.maxSum(nums, dp, i + 1, end))
			
		return dp[start][end]
