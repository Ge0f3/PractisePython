class Node:
    def __init__(self,key):
	  self.left = None
	  self.right = None
	  self.value = key

#Create Root 
root = Node(3)
''' following is the tree after above statement 
	  3 
	/   \ 
     None  None'''
root.left =Node(4)
root.right = Node(2)
''' 4 and 2 become left and right children of 3 
	     3 
	   /   \ 
	  4      2 
     /    \    /  \ 
   None None None None'''
root.left.left  = Node(6); 
root.right.right =Node(1)
'''6 becomes left child of 4 
	     3 
	 /       \ 
	4          2 
    /   \       /  \ 
   6    None  None  1 
  /  \ 
None None'''

def inorder_traversal(root):
	if root:
		#Traverse the left Tree
		inorder_traversal(root.left)
		#print the current value 
		print(root.value,end='-'),
		#Traverse the right Tree
		inorder_traversal(root.right)
def postorder_traversal(root):
	if root:
		#Traverse the left 
		postorder_traversal(root.left)
		#Traverse the right
		postorder_traversal(root.right)
		#print the element
		print(root.value,end="-")
def preorder_traversal(root):
	if root:
		#print the root element
		print(root.value,end="-")
		#Traverse the left 
		preorder_traversal(root.left)
		#Traverse the right
		preorder_traversal(root.right)


# def max_depth(root):
#       if root is None:
#       	return 0
#       else:
#       	l_depth = max_depth(root.left)
#       	r_depth = max_depth(root.right)

#       	if(l_depth>r_depth):
#       		return l_depth+1
#       	else:
#       		return r_depth+1

def max_depth(root):
	if root is None:
		return 0 
	else:
		ldepth = max_depth(root.left)
		rdepth = max_depth(root.right)
	if(ldepth>rdepth):
		return ldepth+1
	else:
		return rdepth+1




if __name__ == "__main__":
    print("Tree Traversal")
    print("Traversing the Tree InOrder")
    inorder_traversal(root)
    print("\n Traversing the Tree PostOrder")
    postorder_traversal(root)
    print("\n Traversing the Tree PreOrder")
    preorder_traversal(root)
    print("The max_depth of the Tree is {}".format(max_depth(root)))