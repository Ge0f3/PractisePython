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
def bubblesort(nums):
	swaps=0
	for i in range(len(nums)):
		for j in range(0,len(nums)-i-1):
			if(nums[j]>nums[j+1]):
				nums[j],nums[j+1]=nums[j+1],nums[j]
				swaps += 1
	return nums,swaps

def main():
	nums = [int(x) for x in input("Enter the array list: ").split(',')]
	#print("The possibility is {}".format(check_possibility(nums)))
	nums,swaps = bubblesort(nums)
	print("The array after bubblesort:\n {}\nNumber of swaps made - {}".format(nums,swaps))

if __name__ == '__main__':
	main()