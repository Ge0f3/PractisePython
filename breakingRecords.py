def breakingRecords(scores):
	high=scores[0]
	low=scores[0]
	high_count = 0
	low_count = 0 
	for x in range(len(scores)):
		if(x==0):
			continue
		if(scores[x]>high):
			high_count += 1
			high = scores[x]
			print("Highest broken")
		if(scores[x]<low):
			low_count +=1
			low=scores[x]
			print("lowest broken")
	return high_count,low_count

def main():
	games=int(input("Enter the number of games: "))
	scores = [int(x) for x in input().split()]
	# print(breakingRecords(scores))
	# high_count,low_count=breakingRecords(scores)
	# print("Number of Time broke the best {} \nNumber of time broke the worst {}".format(high_count,low_count))
	result = breakingRecords(scores)
	print (" ".join(map(str, result)))

if __name__ == '__main__':
	main()