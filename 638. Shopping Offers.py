

class Solution:
	def shoppingOffers(self, price, special, needs):
		dp = dict()
		
		return self.minPrice(price, special, needs, dp)
		
	def minPrice(self, price, special, needs, dp):
		if tuple(needs) in dp:
			return dp[tuple(needs)]
		for offer in special:
			remaining_needs = self.validOffer(offer, needs)
			if remaining_needs != None:
				temp = min(self.fullPrice(price, needs), offer[-1] + self.minPrice(price, special, remaining_needs, dp))
				if tuple(needs) in dp:
					dp[tuple(needs)] = min(temp, dp[tuple(needs)])
				else:
					dp[tuple(needs)] = temp
		if not tuple(needs) in dp:
			dp[tuple(needs)] = self.fullPrice(price, needs)
		return dp[tuple(needs)]
	
	def validOffer(self, offer, needs):
		remaining_needs = [0] * len(needs)
		for i in range(len(offer) - 1):
			if offer[i] > needs[i]:
				return None
			remaining_needs[i] = needs[i] - offer[i]
		
		return remaining_needs		
		
	def fullPrice(self, price, needs):
		result = 0
		for i in range(len(needs)):
			result += (needs[i] * price[i])
			
		return result
		
