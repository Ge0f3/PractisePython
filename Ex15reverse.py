def reverse(string):
	str1 =  string.split(" ")
	string =" ".join(str1[::-1])
	return string
def main():
	string = input("Enter the string which you wanted to be reversed: ")
	string = reverse(string)
	print("The revered string is {}".format(string))
if __name__ == '__main__':
	main()
