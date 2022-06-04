# Python3 program to check
# if a given tree is BST.
import math

# A binary tree node has data,
# pointer to left child and
# a pointer to right child
class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None
        

def check_BST(self): 
    if self.left   :
        print(self.left.data ," left " , self.data)
        if(self.left.data > self.data):
            return False
        else:
            return(check_BST(self.left))

    if self.right:
        if self.right.data < self.data:
            return False
        else:
            return check_BST(self.right)
    return True

    
	
def isBSTUtil(root, prev):
	# traverse the tree in inorder fashion
	# and keep track of prev node
	if (root != None):
		if (isBSTUtil(root.left, prev) == True):
			return False

		# Allows only distinct valued nodes
		if (prev != None and
			root.data <= prev.data):
			return False

		prev = root
		return isBSTUtil(root.right, prev)
	
	return True

def isBST(root):
	prev = None
	return isBSTUtil(root, prev)


#Space optimized answer
INT_MAX = 4294967296
INT_MIN = -4294967296#Function to check whether a Binary Tree is BST or not.

def isBSTSpaceOptimized(node): 
    return (isBSTUtilSpaceOptimized(node, INT_MIN, INT_MAX)) 
      
def isBSTUtilSpaceOptimized( node, mini, maxi): 
          
        #an empty tree is BST so we return true.
		if node is None:
			return True
      
        #returning false if this node violates the min/max constraint.
		if node.data < mini or node.data > maxi:
			return False
      
        #otherwise checking the subtrees recursively.#tightening the min or max constraint.
		return (isBSTUtilSpaceOptimized(node.left, mini, node.data -1) and 
		isBSTUtilSpaceOptimized(node.right, node.data+1, maxi)) 



# Driver Code
if __name__ == '__main__':
	root = Node(3)
	root.left = Node(2)
	root.left.left = Node(1)
	root.right = Node(5)
	root.right.left = Node(4)
	root.right.right = Node(8)
	#root.right.left.left = Node(40)
	flag = 0
	if (check_BST(root)):
		print("Is BST")
	else:
		print("Not a BST")

	#space oiptimized
	if (isBSTSpaceOptimized(root)):
		print("Is BST")
	else:
		print("Not a BST")

# This code is contributed by Srathore
