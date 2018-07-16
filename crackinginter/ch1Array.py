
def unique(arr):
	temp = set(arr)
	res= False
	if(len(arr) == len(temp)):
		return True
	return False

def check_permute(str1,str2):
	str1= list(str1.lower())
	str2= list(str2.lower())
	str1.sort()
	str2.sort()
	permute=False
	if(str1 == str2):
		return True
	return False

def replace_space(sent):
	sent = sent.split(" ")
	sent = "%20".join(sent)
	return sent 

def letter_count(string_count):
	string_count = list(string_count)
	count = dict()
	for letter in string_count:
		count[letter]=count.get(letter,0)+1
	return count
def subString(str1,str2):
	if(len(str1) != len(str2)):
		return False

	str3 = str1+str1

	return str3.find(str2) > -1
	# for i in str1:
	# 	if(i in str2):
	# 		continue
	# 	else:
	# 		return False
	# return True 

def main():
	# string = str(input("Enter a string to see if its unique: "))
	# arr = list(string) 
	# print(unique(arr))
	# str1 = str(input("Enter the first string : "))
	# str2 = str(input("Enter the 2nd string : "))
	# print(check_permute(str1,str2))
	# sent = str(input("Enter a sentence to replace space with %20 : "))
	# print(replace_space(sent))
	# string_count= str(input("Enter a string to for compression : "))
	# print(letter_count(string_count))
	str1 = str(input("Enter the first string : "))
	str2 = str(input("Enter the 2nd string : "))
	print(subString(str1,str2))


if __name__ == '__main__':
	main()