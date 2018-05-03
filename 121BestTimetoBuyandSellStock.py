class solution(object):
	"""docstring for solution"""
	def maxProfit(self,prices):
		if(len(prices)>0):
			mini = min(prices)
			temp = prices[prices.index(mini)+1::]
			if(len(temp)>0):
				maxi= max(temp)
				print("The profit is {}".format(maxi-mini))
			else:
				print("The profit is 0")

	
sol= solution()
lis=[7, 6, 4, 3, 1]
sol.maxProfit(lis)
		