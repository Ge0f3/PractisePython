
import sys

def move_even(nums):
    count =0
    for i in range(len(nums)):
        if(nums[i]%2!=0):
            nums[count],nums[i]=nums[i],nums[count]
            count +=1
    print(nums)
    return "Interchanged"
	
def main():
	print("*****************Move even*****************")
	nums = [int(x) for x in input("Enter the array input: ").split(',')]
	print(move_even(nums))

		
if __name__ == '__main__':
	main()
			