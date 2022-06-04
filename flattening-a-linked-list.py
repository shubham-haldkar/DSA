# https://www.geeksforgeeks.org/flattening-a-linked-list/


class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.down = None


class LinkedList:
    def __init__(self):
        # This is head of the list
        self.head = None

    # Function to insert data 
    def push(self,head,data):
        # Create new node and insert the data
        new_node = Node(data)
        # Make next of new node as head 
        new_node.down = head
        # Move the head to point to new Node
        head = new_node
        return head

 
    def printList(self): 
        temp = self.head
        while(temp != None):
            print(temp.data,end=" ")
            temp = temp.down

 
    # An utility function to merge two sorted linked lists
    def merge(self, a, b):
        # if first linked list is empty then second
        # is the answer
        if(a == None):
            return b
         
        # if second linked list is empty then first
        # is the result
        if(b == None):
            return a
 
        # compare the data members of the two linked lists
        # and put the larger one in the result
        result = None
 
        if (a.data < b.data):
            result = a
            result.down = self.merge(a.down,b)
        else:
            result = b
            result.down = self.merge(a,b.down)
 
        result.right = None
        print(result.data)
        return result
 

    def flatten(self, root):
        print(root.data)
        # Base Case
        if(root == None or root.right == None):
            return root
        # recur for list on right
 
        root.right = self.flatten(root.right)
 
        # now merge
        print(root.right.data)
        root = self.merge(root, root.right)
 
        # return the root
        # it will be in turn merged with its left
        return root
 
# Driver program to test above functions
L = LinkedList()
 
'''
Let us create the following linked list
            5 -> 10 -> 19 -> 28
            |    |     |     |
            V    V     V     V
            7    20    22    35
            |          |     |
            V          V     V
            8          50    40
            |                |
            V                V
            30               45
'''
L.head = L.push(L.head, 30);
L.head = L.push(L.head, 8);
L.head = L.push(L.head, 7);
L.head = L.push(L.head, 5);
 
L.head.right = L.push(L.head.right, 20);
L.head.right = L.push(L.head.right, 10);
 
L.head.right.right = L.push(L.head.right.right, 50);
L.head.right.right = L.push(L.head.right.right, 22);
L.head.right.right = L.push(L.head.right.right, 19);
 
L.head.right.right.right = L.push(L.head.right.right.right, 45);
L.head.right.right.right = L.push(L.head.right.right.right, 40);
L.head.right.right.right = L.push(L.head.right.right.right, 35);
L.head.right.right.right = L.push(L.head.right.right.right, 20);
 
# flatten the list
L.head = L.flatten(L.head);
 
L.printList()