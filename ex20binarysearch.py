def binarysearch(arr,key,left,right):
	while left<=right:
		mid=int((left+right)/2)
		if(arr[mid]==key):
			return True
		elif(key>arr[mid]):
			return binarysearch(arr,key,mid+1,right)
		elif(key<arr[mid]):
			return binarysearch(arr,key,left,mid-1)
	return False

def main():
	print("<------Binary search ------->")
	print("Enter the array elements in order : ")
	arr = [int(x) for x in input().split()]
	key=int(input("Enter the element which you want to search: "))
	result = binarysearch(arr,key,0,len(arr)-1)
	if(result):
		print("{} is found in the array ".format(key))
	else:
		print("{} is not found in the array".format(key))

if __name__ == '__main__':
	main()