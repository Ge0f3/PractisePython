from linkedlist import Node
from linkedlist import singlelinkedlist

def loop_list(l1):
	temp = l1.head
	while (temp):
		print("{}->".format(temp.value),end="")
		temp = temp.next
	print()
def add_ll(l1,l2):
	l3 = singlelinkedlist()
	temp1,temp2=l1.head,l2.head
	while(temp1 or temp2):
		if(temp1 and temp2):
			l3.insert(temp1.value+temp2.value)
			print("{} + {}".format(temp1.value,temp2.value))
			temp1,temp2=temp1.next,temp2.next
		elif temp1:
			l3.insert(temp1.value+0)
			print("{} + {}".format(temp1.value,0))
			temp1 = temp1.next
		elif temp2:
			l3.insert(0+temp2.value)
			print("{} + {}".format(0,temp2.value))
			temp2 = temp2.next
	return l3
def main():
	ll = singlelinkedlist()
	ll.insert(3)
	ll.insert(2)
	ll.insert(1)
	l2= singlelinkedlist()
	l2.insert(7)
	l2.insert(8)
	l3= add_ll(ll, l2)
	loop_list(ll)
	loop_list(l2)
	loop_list(l3)



if __name__ == '__main__':
	main()
