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
		while(temp):
			print("The {} node is {}".format(count,temp.data))
			count += 1
			temp=temp.next
	def isEmpty(self):
		if(self.head is None):
			return "Emtpy"
		else:
			return "Not Empty"
	def getHead(self):
		return self.head.data
		#return self.head is None
	def deleteNode(self,data):
		temp=self.head
		# If the head itself is the data
		if(self.head is not None):
			if(self.head.data == data):
				self.head=temp.next
				temp=None
				print("The node is deleted")
				return True

class students():
	"""docstring for aeroplane"""
	def __init__(self, arg):
		print("This is a collection of students database : ")
	def main():
		student = linkedList()
		student.insertToHead("Geoffrey ")
		student.insertToHead("Amit singh")
		student.insertToHead("Addy")
		student.insertTail("Abhishek kumar")
		student.printList()
		print("The List is {}".format(student.isEmpty()))
		print("The head is at {}".format(student.getHead()))
		student.deleteNode('Addy')
		print("The head is at {}".format(student.getHead()))



	if __name__ == '__main__':
		main()
		
			
		