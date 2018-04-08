class Solution:
	nums = []
	dp = []
	def PredictTheWinner(self, nums):
		if len(nums) < 2:
			return True
		self.nums = nums
		self.dp = [[-1 for j in range(len(nums))] for i in range(len(nums))]
		a_score = self.maximise(0, len(nums) -1)
		b_score = sum(nums) - a_score
		return True if a_score > b_score else False
		
		
		
		
	
	def maximise(self, be, en):
		if be > en:
			return 0
		
		if self.dp[be][en] != -1:
			return self.dp[be][en]
			
		self.dp[be][en] = max(
			min(self.maximise(be + 2, en) + self.nums[be], 
					self.maximise(be + 1, en - 	1) + self.nums[be]),
			min(self.maximise(be + 1, en - 1) + self.nums[en],
					self.maximise(be, en - 2) + self.nums[en]))
		return self.dp[be][en]
		
