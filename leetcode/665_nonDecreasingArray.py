def check_possibility(nums):
	count = 0 
	for i in range(1,len(nums)):
		diff = nums[i-1]-nums[i]
		if(diff<1):
			count += 1
	if(count>2):
		return False
	else:
		return True
def main():
	nums = [int(x) for x in input("Enter the array list: ").split(',')]
	print("The possibility is {}".format(check_possibility(nums)))

if __name__ == '__main__':
	main()