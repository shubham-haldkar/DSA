# https://www.geeksforgeeks.org/check-two-trees-mirror-set-2/
# Python3 code to check two binary trees are
# mirror.
class Node:
 
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
     
# inorder traversal of Binary Tree
def inorder(n, v):
 
    if (n.left != None):
        inorder(n.left, v)        
    v.append(n.data)    
    if (n.right != None):
        inorder(n.right, v) 
 
# Checking if binary tree is mirror
# of each other or not.
def areMirror(a, b):
 
    if (a == None and b == None):
        return True    
    if (a == None or b== None):
        return False 
 
    # Storing inorder traversals of both
    # the trees.
    v1 = []
    v2 = []
    inorder(a, v1)
    inorder(b, v2)
    print(v1)
    print(v2)
 
    if (len(v1) != len(v2)):
       return False
 
    # Comparing the two arrays, if they
    # are reverse then return 1, else 0
    i = 0
    j = len(v2) - 1
  
    while j >= 0:
     
        if (v1[i] != v2[j]):
            return False
        i+=1
        j-=1
     
    return True 
 
# Helper function to allocate a new node
def newNode(data):
    node = Node(data)
    return node
      
# Driver code
if __name__=="__main__":
    a = newNode(1) 
    b = newNode(1) 
     
    a.left = newNode(2) 
    a.right = newNode(3) 
    a.left.left  = newNode(4) 
    a.left.right = newNode(5) 
 
    b.left = newNode(3) 
    b.right = newNode(2) 
    b.right.left = newNode(5) 
    b.right.right = newNode(4) 
 
    if areMirror(a, b):
        print("Yes")
    else:
        print("No")