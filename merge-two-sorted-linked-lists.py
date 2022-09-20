
# https://www.geeksforgeeks.org/merge-two-sorted-linked-lists/
class Node:
    def __init__(self,data) :
        self.data = data
        self.next = None

    
class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.last = None

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

    def addNode(self , data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.last = newNode
            return
        
        self.last.next = newNode
        self.last = newNode

    def mergeLinkedList(listA,listB):
 
        pointerA = listA.head
        pointerB = listB.head

        if(not pointerA):
            return pointerB
        elif(not pointerB):
            return pointerA
        elif(pointerA.data < pointerB.data):
            dummyNode = Node(pointerA.data )
            pointerA = pointerA.next
        else :
            dummyNode = Node(pointerB.data )
            pointerB = pointerB.next
        dummyTail = dummyNode
        print(dummyTail.data)
        while(True): 
            if(pointerA is None):
                dummyTail.next = pointerB
                break
            elif(pointerB is None):
                dummyTail.next = pointerA
            elif(pointerA.data < pointerB.data):
                dummyTail.next = pointerA
                pointerA = pointerA.next
            else :
                dummyTail.next = pointerB
                pointerB = pointerB.next
            dummyTail = dummyTail.next



        return dummyNode

 

listA = LinkedList()
listB = LinkedList()
 
# Add elements to the list in sorted order
listA.addNode(5)
listA.addNode(10)
listA.addNode(15)
 
listB.addNode(2)
listB.addNode(3)
listB.addNode(20)
 

listA.head =listA.mergeLinkedList(listB)
# listA.printList()

        

# Display merged list
print("Merged Linked List is:")
listA.printList()
 