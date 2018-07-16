class Node():
	"""docstring for Node"""
	def __init__(self, data):
		self.data=data
		self.next=None
		
class linkedlist():
	"""docstring for linkedlist"""
	def __init__(self):
		self.head=None
		print("linkedlist created")
	def delete_node(self,data):
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

	def remove_duplicates(self):
		temp1=self.head
		temp2=self.head
		while temp1:
			while temp2.next:
				if(temp1.data == temp2.next.data):
					temp2.next = temp2.next.next
				else:
					temp2=temp2.next
			temp1=temp2=temp1.next
		print("Duplicated removed")

	def last_element(self):
		temp=self.head
		while temp:
			prev=temp
			temp=temp.next
		return prev
				
	def push(self,data):
		new_node = Node(data)
		new_node.next=self.head
		self.head=new_node
	def print_linkedlist(self):
		temp=self.head
		if(temp is None):
			return
		while (temp):
			print("{}".format(temp.data),end="->")
			temp=temp.next
		print()
	def isEmpty(self):
		if(self.head is None):
			return True
		else:
			return False




		