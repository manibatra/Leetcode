class Solution:
	def deleteAndEarn(self, nums):
		if len(nums) < 1:
			return 0
		dict = self.makeDict(nums)
		keys = sorted(list(dict.keys()))
		#print(dict)
		dp = [-1] * len(keys)
		dp[0] = dict[keys[0]]
		self.maxSum(dict, keys, dp, len(keys) - 1)
		return dp[-1]
		
	def maxSum(self, dict, keys, dp, i):
		if i < 0:
			return 0
		if dp[i] != -1:
			return dp[i]
		if keys[i] != keys[i - 1] + 1:
			dp[i] = dict[keys[i]] + self.maxSum(dict, keys, dp, i - 1)
		else:
			dp[i] = max(self.maxSum(dict, keys, dp, i - 1),
							dict[keys[i]] + self.maxSum(dict, keys, dp, i - 2))
		return dp[i]
							
		
		
		
	def makeDict(self, nums):
		nums = sorted(nums)
		dict = {}
		i = 0
		while i < len(nums):
			key = nums[i]
			value = 0
			while i < len(nums):
				 if nums[i] == key:
				 	value += nums[i]
				 	i += 1
				 else:
				 	break;
			#print(value)
			dict[key] = value
		return dict
