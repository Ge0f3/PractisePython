import sys

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


if __name__ == '__main__':
	strOp=StringOperations()
	while(True):
		print("***************************************************************************************")
		print("Type the action as follows")
		print("1.To Check is the string is unique or not ")
		print("2.To generated all possible substring from string")
		print("3.To Replace all the spaces with %20")
		print("4.To check for permutation of 2 string")
		print("5.To check substrings")
		print("6.To exit")
		print("***************************************************************************************")

		user_input = int(input("Enter your option: "))
		if(user_input==1):
			strOp.getString()
			Match=strOp.UniqueString()
			if(Match):
				print("The {} is unique".format(strOp.str1))
			else:
				print("The {} is not Unique".format(strOp.str1))
		elif(user_input==2):
			print("{} of substrings can be generated from the given string".format(strOp.NoOfSubString()))
			strOp.subStrings()
		elif(user_input==4):
			strOp.permutation()
		elif(user_input==3):
			string = str(input("Enter a string to replace all spaces: "))
			strOp.replaceSpace(string)
		elif(user_input==5):
			strOp.check_substr()
		elif(user_input==6):
			print("Exiting !!!")
			sys.exit(0)
		else:
			print("wrong choice Try again !")





		