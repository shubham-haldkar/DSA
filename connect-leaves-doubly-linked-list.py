# https://www.geeksforgeeks.org/connect-leaves-doubly-linked-list/


class Node:     
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def extractLeafList(self):
        elements = []
        print(self.data)
        if(self.left):
            elements += self.left.extractLeafList()
        if (self.right):
            elements += self.right.extractLeafList()
        if(not self.right and not self.left):
            elements.append(self.data)

        return elements








# extractLeafList.head = Node(None)
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)
root.left.left.left = Node(7)
root.left.left.right = Node(8)
root.right.right.left = Node(9)
root.right.right.right = Node(10)
 
print ("Inorder traversal of given tree is:")


print(root.extractLeafList())
# printInorder(root)
 
# root = extractLeafList(root)
 
# print ("\nExtract Double Linked List is:")
# printList(extractLeafList.head)
 
# print ("\nInorder traversal of modified tree is:")
# printInorder(root)