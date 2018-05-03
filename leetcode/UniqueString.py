class StringOperations(object):
	"""docstring for StringOperations"""
	def __init__(self):
		print("This is a class to do String operation !")

	def UniqueString(self):
		Match=True
		for i in range(len(self.str1)):
			for j in range(len(self.str1)):
				if(i==j):
					continue
				elif(self.str1[i]==self.str1[j]):
					Match=False
					return Match
				# else:
				# 	print("Comparing {} with {}".format(self.str1[i],self.str1[j]))
		return Match
	def NoOfSubString(self):

		return (int((len(self.str1)*len(self.str1)+1)/2))

	def permutation(self):
		str1 = str(input("Enter a string: "))
		str2 = str(input("Enter another string to compare: "))
		str1 = ''.join(sorted(str1))
		str2 = ''.join(sorted(str2))
		if(str1==str2):
			print("{} is the permutation of {}".format(str1,str2))
		else:
			print("{} is not the permutation of {}".format(str1,str2))

	def getString(self):
		self.str1=str(input("Enter the string: "))

	def replaceSpace(self,string):
		string = string.split(" ")
		string = "%20".join(string)
		print("The new string is {}".format(string))

	def subStrings(self):
		count = 1
		for i in range(len(self.str1)-1):
			for j in range(i+1,len(self.str1)+1):
				if(len(self.str1[i:j])>0):
					print("String {} - {}".format(count,self.str1[i:j]))
					count += 1
				else:
					continue
	def check_substr(self):
		str1 = str(input("Enter a string: "))
		str2 = str(input("Enter a sub string: "))
		str1 = str1+str1
		if(str2 in str1):
			print("{} is a substring of {}".format(str2,str1))
		else:
			print("{} is a  not substring of {}".format(str2,str1))

strOp=StringOperations()
# while True:
# 	print("*********************************************************************************************")
# 	print("Enter you otpion")
# 	option = str(input("Enter your otpion\n "))

strOp.getString()
Match=strOp.UniqueString()
if(Match):
	print("The string is unique")
else:
	print("The string is not Unique")
print("{} of substrings can be generated from the given string".format(strOp.NoOfSubString()))
strOp.subStrings()
strOp.permutation()
string = str(input("Enter a string to replace all spaces: "))
strOp.replaceSpace(string)
strOp.check_substr()



		