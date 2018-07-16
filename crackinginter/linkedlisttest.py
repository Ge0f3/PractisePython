from linkedlist import linkedlist

def createlist():
	student =linkedlist()
	# 12->11->12->21->41->43->21
	student.push(21)
	student.push(3)
	student.push(43)
	student.push(41)
	student.push(21)
	student.push(12)
	student.delete_node(43)
	student.push(11)
	student.push(12)
	student.print_linkedlist()
	print("The last element in the linkedList is {}".format(student.last_element().data))
	student.remove_duplicates()
	student.print_linkedlist()


def main():
	createlist()

if __name__ == '__main__':
	main()