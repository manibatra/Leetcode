class Solution:
	def maxCoins(self, nums):
		if len(nums) < 1: 
			return 0
		if len(nums) == 1:
			return nums[0]
		sums = {}
		return self.maxSum(nums, sums)
		
		
	def maxSum(self, nums, sums):
		if len(nums) == 2:
			return (nums[0] * nums[1]) + max(nums)
		if tuple(nums) in sums:
			return sums[tuple(nums)]
		max_sum = 0
		max_index = 0
		#print(nums)
		for i in range(len(nums)):
			if i == 0:
				current_sum = (1 * nums[i] * nums[i + 1])
			elif i == len(nums) - 1:
				current_sum = (nums[i - 1] * nums[i] * 1)
			else:
				current_sum = (nums[i - 1] * nums[i] * nums[i + 1])
			
			new_list = nums[:]
			new_list.pop(i)
			#print(nums, new_list)
			total_sum = current_sum + self.maxSum(new_list, sums)
			
			if total_sum > max_sum:
				max_sum = total_sum
				max_index = i
		
		sums[tuple(nums)] = max_sum
		return max_sum
