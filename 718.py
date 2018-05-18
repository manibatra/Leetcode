import itertools
class Solution:
	def findLength(self, A, B):
        i = 1
        j = 1
        dp = [[0 for j in range(len(B) + 1)] for i in range(len(A) + 1)]
        while i < (len(A) + 1):
            j = 1
            while j <  (len(B) + 1):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = 0
                j += 1
            i += 1
        #print(dp)
        return max(list(itertools.chain.from_iterable(dp)))
