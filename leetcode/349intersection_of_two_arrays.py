def intersection(nums1,nums2):

	inter = set()
	for num1 in nums1:
		for num2 in nums2:
			if(num1==num2):
				inter.add(num2)

	return list(inter)

def main():
	nums1 = [ int(x) for x in input('Enter nums for nums1: ').split(',')]
	nums2 = [ int(x) for x in input('Enter nums for nums2: ').split(',')]
	print("The intersection of  {} and {} is \n {}".format(nums1,nums2,intersection(nums1,nums2)))

if __name__ == '__main__':
	main()