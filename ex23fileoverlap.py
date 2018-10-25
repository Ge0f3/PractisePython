
def fileoverlap():
	file1 = '/Users/geofe/Documents/workspace/PractisePython/happynumbers.txt' 
	file2 = '/Users/geofe/Documents/workspace/PractisePython/primenumbers.txt' 
	file3 = '/Users/geofe/Documents/workspace/PractisePython/comman.txt' 
	numbers = dict()
	file1 = open(file1,'r')
	file2=open(file2,'r')
	common =list()
	for line in file1:
		numbers[int(line)]=numbers.get(int(line),0)+1

	for line in file2:
		numbers[int(line)]=numbers.get(int(line),0)+1
	
	# print("\n \n The dictonary is {}".format(numbers))

	for value in numbers.items():
		if(value[1]>1):
			common.append(value[0])

	print("\n \n The common values are {}".format(common))

	file3 = open(file3,'w+')
	file3.write("The common Numbers are : \n")
	for num in common:
		file3.write("{} \n".format(str(num)))


def main():
	print("<-------Ex 23 File overlap program ------->")
	fileoverlap()



if __name__ == '__main__':
	main()