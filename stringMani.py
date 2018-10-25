def stringMani(string):
	New_string = ""
	for i in range(0,len(string),2):
		New_string = New_string + string[i]*int(string[i+1])
		print(string[i]*int(string[i+1]))
	return New_string

def main():
	string  = str(input("Enter a string "))
	#stringMani(string)
	print("The Generated new String is {} ".format(stringMani(string)))
if __name__ == '__main__':
	main()