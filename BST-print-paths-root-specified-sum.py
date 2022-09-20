# https://www.geeksforgeeks.org/print-paths-root-specified-sum-binary-tree/

# Python3 program to Print all the paths from root, with a specified sum in Binary tree
	
# Binary Tree Node
""" utility that allocates a Node
with the given data """
class Node:
	# Construct to create a Node
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

# function to print path 
def printNodes(path):
    print("Path is " ,end="  ")
    for i in path:
        print(i , end=" ")
    print()


# This function prints all paths
# that have sum k
def printPathsUtil(curr_node, sum, sum_so_far, path):
    if(not curr_node):
        return
    
    sum_so_far += curr_node.data
    path.append(curr_node.data)

    if(sum_so_far == sum):
        printNodes(path)
    
    # If there is left child then traverse it
    if(curr_node.left):
        printPathsUtil(curr_node.left , sum,sum_so_far , path)
    # If there is right child then traverse it
    if(curr_node.right):
        printPathsUtil(curr_node.right , sum,sum_so_far , path)

    #remove curr element from path
    path.pop()

 
# A wrapper over printKPathUtil()
def printPaths(root, sum):

	path = []
	printPathsUtil(root, sum, 0, path)

# Driver Code
if __name__ == '__main__':

	"""   10
	     /	 \
    	28	 13
		/	 \
		14	 15
		/ \	 / \
	   21 22 23 24"""
	root = Node(10)
	root.left = Node(28)
	root.right = Node(13)

	root.right.left = Node(14)
	root.right.right = Node(15)

	root.right.left.left = Node(21)
	root.right.left.right = Node(22)
	root.right.right.left = Node(23)
	root.right.right.right = Node(24)

	sum = 38

	printPaths(root, sum)

 
