
import sys

def move_zeros(nums):
	count = 0 
	for i in range(len(nums)):
		if(nums[i]!=0):
			nums[count]=nums[i]
			count +=1
	print(count)
	# while count<len(nums):
	# 	nums[count] = 0
	# 	count+=1
	# return nums
	# count = 0 # Count of non-zero elements 
	# for i in range(len(nums)): 
	# 	if arr[i] != 0: 
	# 		arr[count] = arr[i] 
	# 		count+=1
	# while count < n: 
	# 	arr[count] = 0
	# 	count += 1

	
def main():
	print("*****************Move zeros*****************")
	nums = [int(x) for x in input("Enter the array input: ").split(',')]
	print(move_zeros(nums))
	print(nums)

		
if __name__ == '__main__':
	main()