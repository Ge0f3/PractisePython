class Node():
    def __init__(self, val):
        self.val = val
        self.next = None
class LinkedList():
    def __init__(self, head=None):
        self.head = head
        self.size = 0

    def travel(self):
        temp = self.head
        while(temp):
            print(temp.val, end="->")
            temp = temp.next
        print()

    def getNth(self,N):
        if(self.head is None or N>=self.size):
            return -1
        temp = self.head
        for i in range(N):
            temp = temp.next
        return temp.val
    
    def push(self,val):
        new_node = Node(val)
        new_node.next= self.head
        self.head = new_node
        self.size +=1

    def append(self,val):
        new_node = Node(val)
        
        #If the linkedlist is empty
        if self.head is None:
            self.head = new_node
            self.size +=1
            return 
            print("Inserted")
        
        #Else travel till the last and extend it to the last node
        last_node = self.head
        while(last_node.next):
            last_node = last_node.next
        last_node.next = new_node
        self.size +=1
        print("Inserted")

    #inserting a node at an index
    def insertAtIndex(self,index,val):
        if(index<0 or index>self.size):
            print("Value cannot be inserted at this position")
            return 
        if(index == 0):
            self.push(val)
        else:
            new_node = Node(val)
            curr = self.head
            prev = None
            for i in range(index-1):
                prev = curr
                curr = curr.next
            prev.next = new_node
            new_node.next = curr
            self.size +=1

    def deleteAll(self,val):
        temp = self.head
        while(temp):
            if(temp.val ==val):
                self.delete(val)
                temp = temp.next
            else:
                temp = temp.next
        


    #Delete and Node from the list 
    def delete(self,value):
        temp = self.head
        #if head itself has to be removed
        if(temp is not None):
            if(temp.val == value):
                self.head = temp.next
                temp =None
                return 

        while(temp is not None):
            if(temp.val == value):
                break
            prev = temp
            temp = temp.next

        if temp is None:
            return 
        prev.next = temp.next
        temp= None
    def isPalindrome(self):
        """
        :type head: ListNode
        :rtype: bool
        """
        llist = []
        temp = self.head
        while(temp):
            llist.append(temp.val)
            temp = temp.next 
        
        while(self.head):
            pop_item = llist.pop()
            if(self.head.val != pop_item):
                return False
            self.head = self.head.next
        if(not llist):
            return True
        else:
            return True

    def deleteAtindex(self,index):
        if(index<0 or index>self.size):
            return 

        curr = self.head()
        if index==0:
            self.head = curr.next
        else:
            for i in range(index):
                curr = curr.next
            curr.next = curr.next.next
            self.size -= 1

        

def main():
    llist = LinkedList()
    
    # llist.push(20)
    # llist.travel()
    # llist.push(10)
    # llist.travel()
    # llist.push(0)
    # llist.append(0)
    # llist.travel()
    # llist.delete(20)
    # llist.insertAtIndex(0,22)
    # llist.insertAtIndex(5,21)
    # llist.insertAtIndex(3,24)
    # llist.travel()
    # # llist.delete(40)
    # #llist.travel()
    
    # #print("Is the linked list palindrome - {}".format(llist.isPalindrome()) )
    # print("The 2nd element in the LList is {}".format(llist.getNth(2)))
    # print("The size of the linked list is {}".format(llist.size))
    # llist.travel()
    # llist.deleteAll(0)
    # llist.travel()

    llist.push(1)
    llist.push(1)
    llist.travel()
    llist.deleteAll(1)
    llist.travel()
if __name__ == '__main__':
    main()
    
        