# https://www.geeksforgeeks.org/how-to-determine-if-a-binary-tree-is-balanced/



class Node:
    def __init__(self,data) :
        self.data = data
        self.left = None
        self.right = None


def height(self):
    if self == None:
        return 0
     
    temp = (max(height(self.right) , height(self.left)))
    return temp +1
def isBalancedTree(self):
    if( not self):
        return True
    
    lHeight =  height(self.left)
    rHeight =  height(self.right)
    if( (abs(lHeight-rHeight) <=1) and (isBalancedTree(self.left))
        and (isBalancedTree(self.right))) :
        return True
    return False


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.left.left.left = Node(7)
if isBalancedTree(root):
    print("Tree is balanced")
else:
    print("Tree is not balanced")