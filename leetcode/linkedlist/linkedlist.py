class Node(object):
	"""docstring for Node"""
	def __init__(self, value):
		self.value=value
		self.next =None
	def get_value(self):
		return self.value
	def get_next(self):
		return self.next
	def set_next(self,new_node):
		self.next=new_node

class singlelinkedlist(object):
	"""docstring for singlelinkedlist"""
	def __init__(self,head=None):
		print("Single linked list created")
		self.head=head

	def insert(self,data):
		new_node =Node(data)
		new_node.set_next(self.head)
		self.head=new_node

	def print_list(self):
		temp =self.head
		while temp:
			print("{}->".format(temp.value),end='')
			temp=temp.get_next()
		print()

	def size(self):
		current= self.head
		size=0
		while(current):
			size += 1
			current= current.get_next()
		return size 

	def search(self,data):
		current=self.head
		found = False
		while current and not found:
			if current.get_value()==data:
				found = True
			else:
				current=current.get_next()

		if current is None:
			print ("The value is not in the list")
		else:
			print ("The value is in the list")

	def delete(self,data):
		current=self.head
		previous = None
		found=False
		while current and not found:
			if current.get_value()==data:
				found = True
			else:
				previous=current
				current=current.get_next()
		if current is None:
			print("The value is not in the list")
		elif previous is None:
			self.head = current.get_next()
		else:
			previous.set_next(current.get_next())

	def remove_duplicates(self):
		outer=self.head
		while outer:
			inner=outer.next
			while inner:
				if(outer.value==inner.value):
					self.delete(inner.value)
				inner=inner.get_next()
			outer=outer.get_next()

	def kth_element(self,k):

		size = self.size()

		if(size<1):
			return "List empty"
		elif (k>size):
			return "K is greater than list size"

		temp = self.head

		for i in range(1,size-k+1):
			temp = temp.next

		return temp.value





		