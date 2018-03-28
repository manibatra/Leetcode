class Solution:
	def countSubstrings(self, s):
		ans = [0] * len(s)
		ans[0] = 1
		
		for i in range(1, len(s)):
			# adding the number of substrings so far
			ans[i] += ans[i - 1]
			
			# adding one to ans for the char itself
			ans[i] += 1
			
			# make a pass through the entire string once
			# reverse
			temp = s[:i+1]	
			for j in range(0, i):
				sub_string = temp[-(j+2):]
				if sub_string == sub_string[::-1]:
					ans[i] += 1
				
		return ans[- 1]
