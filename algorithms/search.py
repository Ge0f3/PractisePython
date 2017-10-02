class search():
	"""docstring for search"""
	def __init__(self):
		self.array=list(map(int,input('Enter the elements for the array: ').split()))

	def printarray(self):
		print("The array is {}".format(self.array))
	def bubble_sort(self):
		for i in range(len(self.array)):
			for j in range(len(self.array)):
				if(self.array[i]<self.array[j]):
					self.array[j],self.array[i]=self.array[i],self.array[j]
	def linearsearch(self,search_term):
		found = False
		for i in range(len(self.array)):
			if(self.array[i]==search_term):
				found=True
				break
		if(found):
			print("The number {} was found and was in the position {}".format(search_term,i+1))
		else:
			print("The element was not in the list ")
	def binary_search(self,search_term):
		low=0
		high=len(self.array)-1
		found=False
		while(low<=high):
			mid=int((low+high)/2)
			if(self.array[mid]==search_term):
				found=True
				break
			elif(search_term>self.array[mid]):
				low=mid+1
			else:
				high=mid-1
		if(found):
			print("The number {} was found and was in the position {}".format(search_term,mid+1))
		else:
			print("The element is not found in the list.")



search =search()
#search.bubble_sort()
#print(len(search.array))
search.printarray()
search_term=int(input("Enter the term to search : "))
option=int(input("Which method you want to use \n 1.Binary search \n 2.Linear search\n"))
if(option==1):
	search.binary_search(search_term)
elif(option==2):
	search.linearsearch(search_term)	

		