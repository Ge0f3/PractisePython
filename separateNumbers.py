

def seperateNumber(n):
	for i in range(len(n)):
		if(i==0):
			continue
		else:
			if((int(n[i])-int(n[i-1])==1)):
				#print("{} - {} is {}".format(n[i],n[i-1],int(n[i])-int(n[i-1])))
				#print("Its equl to 1")
				continue
			else:
				#print("No its not")
				return False
	return True
			#print("{} - {} is {}".format(n[i],n[i-1],int(n[i])-int(n[i-1])))
	# for i in range(int(len(n)/2)):
	# 	for i in range(len(n)):
	# 		if(int(n[i-1])-int(n[i])==1):
	# 			continue
	# 		else:
	# 			return False
	# return True


def main():
	num=str(input("Enter the Number : "))
	if(seperateNumber(num)):
		print("It's Beautiful")
	else:
		print("It's not Beautiful")


if __name__ == '__main__':
	main()