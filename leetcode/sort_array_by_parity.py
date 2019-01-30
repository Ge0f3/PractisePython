
import sys

def move_zeros(nums):
	count = 0 
	arr = nums
	n = len(arr)
	temp = []
	j=0
	for i in range(len(arr)): 
		if arr[i]%2 == 0: 
			temp.append(arr[count])
			arr[count] = arr[i] 
			count+=1
	while count < n: 
		arr[count] = temp[j]
		count += 1
		j+=1
	print(temp)
	
def main():
	print("*****************Sort By Parity *****************")
	nums = [int(x) for x in input("Enter the array input: ").split(',')]
	print(move_zeros(nums))
	print(nums)

		
if __name__ == '__main__':
	main()