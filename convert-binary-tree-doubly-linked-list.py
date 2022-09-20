 

# https://www.geeksforgeeks.org/convert-given-binary-tree-doubly-linked-list-set-3/


class Node:
    def __init__(self , data) -> None:
        self.data = data
        self.right = None
        self.left = None


class DoublyLinkedLIst:
    def __init__(self) -> None:
        self.head = None
        self.tail  = None

    def convertBTtoDLL(self , root):
        if(root == None):
            return
        
        # recursively traverse in left subtree
        self.convertBTtoDLL(root.left)

        # convert BT node to linked list node
        node = root
        if self.head is None:
            self.head = node
        else:
            self.tail.right = node
            node.left = self.tail
        self.tail = node

        # traverse in right subtree
        self.convertBTtoDLL(root.right)

        # return the head of doubly linked list
        return self.head

def BinaryTree2DoubleLinkedList(root):
    dll = DoublyLinkedLIst()
    return dll.convertBTtoDLL(root)


def print_dll(head):
    '''Function to print nodes in given doubly linked list'''
    while head is not None:
        print(head.data, end=" ")
        head = head.right


if __name__ == "__main__":
   
    # Let us create the tree as
    # shown in above diagram
    root = Node(10)
    root.left = Node(12)
    root.right = Node(15)
    root.left.left = Node(25)
    root.left.right = Node(30)
    root.right.left = Node(36)
     
    # convert to DLL
    head = BinaryTree2DoubleLinkedList(root)
     
    # Print the converted list
    print_dll(head)
     


