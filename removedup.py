class Node():
	"""docstring for Node"""
	def __init__(self,data):
		self.data=data
		self.next = None

class Linkedlist():
	"""docstring for Linkedlist"""
	def __init__(self):
		self.head=None

	def insert(self,data):
		new_node =Node(data)
		new_node.next=self.head
		self.head = new_node

	def removeDup(self):
		current=second=self.head
		while current is not None:
			while second.next is not None:
				if(second.next.data == current.data ):
					second.next= second.next.next
				else:
					second= second.next
			current=second=current.next
	def lastbefore(self):
		temp = self.head
		prev = None
		while(temp.next is not None):
			prev = temp 
			temp= temp.next

		print("The last before element is {}".format(prev.data))

	# def printlist(self):
	# 	temp = self.head
	# 	while temp is not None:
	# 		print("The node is {}".format(temp.data))
	# 		temp= temp.next
	def getLength(self):
		count = 0
		temp=self.head
		while (temp is not None):
			count += 1
			temp=temp.next
		return count 
	def printlist(self,lenght=None):
		if lenght is None:
			temp = self.head
			while temp is not None:
				print("The node is {}".format(temp.data))
				temp= temp.next

		else:
			temp = self.head
			while temp is not None:
				print("The node is {} at position {}".format(temp.data,lenght))
				temp= temp.next
				lenght = lenght-1

class numbers(object):
	"""docstring for numbers"""
	def main():
		num = Linkedlist()
		num.insert(12)
		num.insert(13)
		num.insert(14)
		num.insert(15)
		num.insert(16)
		num.insert(17)
		num.insert(18)
		num.insert(19)
		num.insert(21)
		num.insert(22)
		num.insert(23)
		num.insert(24)
		print("The linked list before removing duplicates")
		num.printlist()
		num.lastbefore()
		print("The lenght of the linked list is {}".format(num.getLength()))
		lenght = num.getLength()
		print("The linked list before removing duplicates")
		num.removeDup()
		num.printlist(lenght)

	if __name__ == '__main__':
		main()


		

		
		
		