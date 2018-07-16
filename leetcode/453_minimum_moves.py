def find_min_moves(arr):
	min_e =min(arr)
	min_moves = sum(arr)-min_e*len(arr)
	return min_moves

if __name__ == '__main__':
	arr = [int(x) for x in input("Enter the array elements: ").split(",")]
	print("The minimum moves is {}".format(find_min_moves(arr)))