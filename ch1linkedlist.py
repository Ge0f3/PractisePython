class node():
	"""docstring for node"""
	def __init__(self, data):
		self.data = data
		self.next=None
class linkedList():

	def __init__(self):
		self.head = None
	def insertToHead(self,data):
		newnode = node(data)
		newnode.next=self.head
		self.head = newnode

	def insertTail(self,data):
		newnode=node(data)
		n=self.head
		while(n.next!=None):
			n=n.next
		n.next=newnode
	def printList(self):
		temp=self.head
		count=1
		if(temp is None):
			print("The list is empty")
			return 
		while(temp):
			print("The {} node is {}".format(count,temp.data))
			count += 1
			temp=temp.next
	def isEmpty(self):
		if(self.head is None):
			return True
		else:
			return False
	def getHead(self):
		return self.head.data
		#return self.head is None
	def deleteNode(self,data):
		temp=self.head
		# If the head itself is the data
		if(self.head is not None):
			if(temp.data == data):
				self.head=temp.next
				temp=None
				print("{} is deleted".format(data))
				return True

		prev = None
		while(temp is not None and temp.data != data):
			prev = temp
			temp = temp.next
		if(temp is None):
			print("The {} is not present in the node".format(data))
			return 
		# if temp is note none then it was present and got exited from the while loop 

		prev.next = temp.next
		temp = None
		print("{} is deleted".format(data))


 

class students():
	"""docstring for aeroplane"""
	def __init__(self, arg):
		print("This is a collection of students database : ")
	def main():
		student = linkedList()
		student.insertToHead("Geoffrey")
		student.insertToHead("Amit singh")
		student.insertToHead("Addy")
		student.insertTail("Abhishek_kumar")
		student.printList()
		print("The List is {}".format(student.isEmpty()))
		print("The head is at {}".format(student.getHead()))
		student.deleteNode('Addy')
		print("The head is at {}".format(student.getHead()))
		choice = 'y'
		while(choice == 'y'):
			node_delete= str(input("Enter a node to delete : "))
			student.deleteNode(node_delete)
			#print("The head is at {}".format(student.getHead()))
			choice = str(input("Do you want to delete \nif type y else leave blanck to exit: ")).lower()

			
		student.printList()

	if __name__ == '__main__':
		main()
		
			
		