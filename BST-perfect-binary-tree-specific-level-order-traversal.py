# https://www.geeksforgeeks.org/perfect-binary-tree-specific-level-order-traversal/

class Node:
    def __init__(self , data) -> None:
        self.data = data
        self.left = None
        self.right= None 


    # from Top to Bottom
    # 4  5  6  7
    # print  -  4 7  5 6 
    # 4(left), 7(right), 5(left), 6(right) 
    def printSpecificLevelTraversal(self):
        if Node is None:
            return

        # print root node
        print(self.data , end=" ")

        #print that left exists
        if(self.left):
            print(self.left.data , end=" ")
            print(self.right.data , end=" ")
        
        # check if left of left exists otherwise return
        if(self.left.left is None):
            return

        # create a queue to store childrens of nodes
        queue = []

        queue.append(self.left)
        queue.append(self.right)

        # We process two nodes at a time, so we need
        # two variables to store two front items of queue
        first = None
        second = None

        while(len(queue) > 0):
            first = queue.pop(0)
            second = queue.pop(0)

            # Print children of first and second in reverse order
            print (first.left.data,end=" ")
            print (second.right.data,end=" ")
            print (first.right.data,end=" ")
            print (second.left.data,end=" ")

                    # If first and second have grandchildren,
            # enqueue them in reverse order
            if first.left.left is not None:
                queue.append(first.left)
                queue.append(second.right)
                queue.append(first.right)
                queue.append(second.left)
 

      
                


  # from Top to Bottom
    # print reverse from bottom to top
     
def specific_level_order_traversal(root) :
 
    # for level order traversal
    q = []
     
    # Stack to print reverse
    s = []
     
    q.append(root)
    sz = 0
     
    while(len(q) > 0) :
     
        # vector to store the level
        v = []
        sz = len(q) # considering size of the level
        i = 0
        while( i < sz) :
         
            temp = q.pop(0)
            
             
            # push data of the node of a
            # particular level to vector
            v.append(temp.data)
             
            if(temp.left != None) :
                q.append(temp.left)
     
            if(temp.right != None) :
                q.append(temp.right)
         
            i = i + 1
         
        # push vector containing a level in Stack
        s.append(v)
     
    # print the Stack
    while(len(s) > 0) :
     
        # Finally pop all Nodes from Stack
        # and prints them.
        v = s[-1]
        s.pop()
        i = 0
        j = len(v) - 1
        while( i < j) :
            print(v[i] , " " , v[j] ,end= " ")
            j = j - 1
            i = i + 1
             
    # finally print root
    print(root.data)


# Perfect Binary Tree of Height 4
root = Node(1)
  
root.left= Node(2)
root.right   = Node(3)
  
root.left.left  = Node(4)
root.left.right = Node(5)
root.right.left  = Node(6)
root.right.right = Node(7)
  
root.left.left.left  = Node(8)
root.left.left.right  = Node(9)
root.left.right.left  = Node(10)
root.left.right.right  = Node(11)
root.right.left.left  = Node(12)
root.right.left.right  = Node(13)
root.right.right.left  = Node(14)
root.right.right.right  = Node(15)
  
root.left.left.left.left  = Node(16)
root.left.left.left.right  = Node(17)
root.left.left.right.left  = Node(18)
root.left.left.right.right  = Node(19)
root.left.right.left.left  = Node(20)
root.left.right.left.right  = Node(21)
root.left.right.right.left  = Node(22)
root.left.right.right.right  = Node(23)
root.right.left.left.left  = Node(24)
root.right.left.left.right  = Node(25)
root.right.left.right.left  = Node(26)
root.right.left.right.right  = Node(27)
root.right.right.left.left  = Node(28)
root.right.right.left.right  = Node(29)
root.right.right.right.left  = Node(30)
root.right.right.right.right  = Node(31)
  
print ("Specific Level Order traversal of binary tree is")
# root.printSpecificLevelTraversal()
root.printSpecificLevelTraversal23()
 


        