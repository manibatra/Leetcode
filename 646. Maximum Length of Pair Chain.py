class Solution:
	def findLongestChain(self, pairs):
		sorted_pairs = sorted(pairs, key = lambda x : x[1])
		#print(sorted_pairs)
		max_length = 1
		max_number = sorted_pairs[0][1]
		
		if len(pairs) == 1:
			return 1
			
		for i in range(1, len(sorted_pairs)):
			if sorted_pairs[i][0] > max_number:
				max_length += 1
				max_number = sorted_pairs[i][1]
		
		return max_length
