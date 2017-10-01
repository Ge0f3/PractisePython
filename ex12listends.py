class listend():
	def __init__(self):
		print("Lets try out printing list end ")
	def listend(self,lis):
		return [self.lis[0],self.lis[len(lis)-1]]
	def getlist(self):
		self.lis=str(input("Enter the list : "))
		if(self.lis.find(',')>0):
			self.lis=self.lis.split(",")
		else:
			self.lis=self.lis.split()
lisen=listend()
lisen.getlist()
print("The first and the last element in the list is {}".format(lisen.listend(lisen.lis)))