
import sys

def find_pivot(nums):
	s = sum(nums)
	left_sum= 0 
	for i,elem in enumerate(nums):
		if(left_sum == s-left_sum-elem):
			return i 
		left_sum += elem
	return -1

def main():
	print("*****************Find Pivot*****************")
	nums = [int(x) for x in input("Enter the array input: ").split(',')]
	print("The pivot element is at the index {}".format(find_pivot(nums)))

		
if __name__ == '__main__':
	main()