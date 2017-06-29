class primeOrnot():
	"""docstring for primeOrnot"""
	def __init__(self):
		self.number=int(input("Enter a number : "))
	def check(self,number):
		exception=[0,1,2]
		if(number in exception):
			print("{} is Prime ".format(number))
		else:
			for i in range(2,number):
				if(number%i==0):
					print("{} is not Prime".format(number))
					break
			if(i+1==number):
				print("{} is prime".format(number))
		
checkprime=primeOrnot()
checkprime.check(checkprime.number)