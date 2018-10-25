def removeduplicates(lis):
	#print("calling removeduplicates")
	new_list = list()
	for item in lis:
		if item in new_list:
			continue
		else:
			new_list.append(item)
	return new_list
def removeduplicate(lis):
	#print("calling removeduplicate")
	lis=set(lis)
	lis=list(lis)
	return lis
lis = ["Michele", "Robin", "Sara", "Michele"]
print("Lets remove duplicate from the list {}".format(lis))
lis =  removeduplicates(lis)
print("The list after removing duplicates from the list is \n {}".format(lis))




	