def reversewordoreder(string):
	string1=string.split(" ")
	string1=string1[::-1]
	string=" ".join(string1)
	return string

def getstring():
	string=str(input("Enter a sentence :"))
	return string

string=getstring()
print(reversewordoreder(string))