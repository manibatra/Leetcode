class Solution:
	def combinationSum4(self, nums, target):
		if target == 0 or len(nums) == 0:
			return 0
		sums = {}
		return self.treeSum(target, nums, sums)
	
	
	def treeSum(self, sum, nums, sums):
		if sum == 0:
			return 1
		if sum < 0:
			return 0
		if sum in sums:
			return sums[sum]
		no_of_ways = 0
		for i in range(len(nums)):
			if nums[i] <= sum:
				no_of_ways += self.treeSum(sum - nums[i], nums, sums)
		sums[sum] = no_of_ways
		return sums[sum]
