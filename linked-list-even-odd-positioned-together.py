# https://www.geeksforgeeks.org/rearrange-a-linked-list-such-that-all-even-and-odd-positioned-nodes-are-together/

from email import header


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) :
        self.head = None


    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def rearrangeEvenOdd(self , head):
        oddHead = self.head
        evenHead = self.head.next

        evenFirst = evenHead
        temp = True
        while(temp):
            if (oddHead == None or evenHead==None or evenHead.next==None):
                oddHead.next = evenFirst
                temp = False
                break
            oddHead.next = evenHead.next
            oddHead =  evenHead.next

            if(oddHead.next ==None ):
                evenHead.next = None
                oddHead.next = evenFirst
                temp = False
                break
            evenHead.next = oddHead.next
            evenHead = oddHead.next
        return head

     
    # A utility function to print a linked list
    def printlist(self, node):
        while (node != None):
            print(node.data, end = "")
            print("->", end = "")
            node = node.next
        print ("NULL")

            
    
        
# Driver code
ll = LinkedList()
ll.push(5)
ll.push(4)
ll.push(3)
ll.push(2)
ll.push(1)
print ("Given Linked List")
ll.printlist(ll.head)
 
start = ll.rearrangeEvenOdd(ll.head)
 
print ("\nModified Linked List")
ll.printlist(start)