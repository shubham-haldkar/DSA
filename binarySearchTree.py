# max width 
# 


import numbers

class BinarySearchTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
    # Check given tree in BST or not
    def isBST_1(self, root):
        #code here
        ele = self.inOrderTraversal()
        for i in range (1,len(ele)):
            if(ele[i-1] > ele[i]):
                return False
        return True

    def check_BST(self): 
        if self.left   :
            if(self.left.data > self.data):
                return False
            else:
               return self.left.check_BST()

        if self.right:
            if self.right.data < self.data:
                return False
            else:
                return self.right.check_BST()
        return True


    def addChild(self,data):
        if data == self.data:
            return
        
        if data<self.data:
            # add data in left subtree
            if self.left:
                self.left.addChild(data)
            else:
                self.left = BinarySearchTreeNode(data)
        
        else:
            if self.right:
                self.right.addChild(data)
            else:
                self.right = BinarySearchTreeNode(data)


    def inOrderTraversal(self):
        elements =[]

        #visit left tree
        if self.left:
            elements += self.left.inOrderTraversal()

        #visit base node
        elements.append(self.data)        

        # visit right node
        if self.right:
            elements += self.right.inOrderTraversal()
        return elements

    def pre_order_traversal(self):
        elements = [self.data]
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()

        return elements
    
    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)

        return elements
    
    def search(self,val):
        if self.data==val:
            return True
        
        if val< self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    # function to delete node using right subtree
    def delete(self,val):
        if val<self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val>self.data:
            if self.right:
                self.right = self.right.delete(val)
        else :
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            
            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)

        return self

    # Function uses left subtree to delete node
    def delete_left(self,val):
        if val<self.data:
            if self.left:
                self.left = self.left.delete_left(val)
        elif val>self.data:
            if self.right:
                self.right = self.right.delete_left(val)
        else :
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            
            max_val = self.left.find_max()
            self.data = max_val
            self.left = self.left.delete_left(max_val)

        return self

    def calculate_sum(self):
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        return self.data + left_sum + right_sum

    # Traverses the tree in in-order form and
    # populates a hashMap that contains the
    # vertical sum
    def verticalSumUtil(self, hd, Map):
        if(self == None):
            return
        if(hd in Map.keys()):
            Map[hd] = Map[hd] + self.data
        else:
            Map[hd] = self.data

        #visit left tree
        if self.left:
            self.left.verticalSumUtil(hd-1, Map)               
        # visit right node
        if self.right:
            self.right.verticalSumUtil(hd+1, Map)
 
    #vertical sum of tree
    def vertical_sum(self): 
        # a dictionary to store sum of
        # nodes for each horizontal distance
        Map = {}         
        # Populate the dictionary
        self.verticalSumUtil(0, Map)
      
        # Prints the values stored
        # by VerticalSumUtil()

        for i,j in Map.items():
            print(i, "=", j, end = ", ")

    def lca(root, n1, n2):
        while root:
            # If both n1 and n2 are smaller than root,
            # then LCA lies in left
            if root.data > n1 and root.data > n2:
                root = root.left
            
            # If both n1 and n2 are greater than root,
            # then LCA lies in right
            elif root.data < n1 and root.data < n2:
                root = root.right
            else:
                break    
        return root

    # UTILITY FUNCTIONS
    # Compute the "height" of a tree -- the number of
    # nodes along the longest path from the root node
    # down to the farthest leaf node.


    
    def getMaxWidth(root):
        maxWidth = 0
        h = height(root)
        # print (h)
        # Get width of each level and compare the
        # width with maximum width so far
        for i in range(1, h+1):
            width = root.getWidth(i)
            if (width > maxWidth):
                maxWidth = width
        
        print(maxWidth)
        return maxWidth
    
    # Get width of a given level 
    def getWidth(root, level):
        print(root.data)
        if root is None:
            return 0
        if level == 1:
            return 1
        elif level > 1:
            return (root.left.getWidth( level-1) + 
                root.right.getWidth( level-1))
 

def height(node):
    if node is None:
        return 0
    else:
    
        # compute the height of each subtree
        lHeight = height(node.left)
        rHeight = height(node.right)

        # use the larger one
        return (lHeight+1) if (lHeight > rHeight) else (rHeight+1)

def buildTree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.addChild(elements[i])
    
    return root

if __name__ == '__main__':
    numbers = [4,2,6,1,3,7,5]
    numbersTree = buildTree(numbers)
    # numbersTree.getMaxWidth()

    # print(numbersTree.check_BST())

    print(numbersTree.inOrderTraversal())
    # # print( numbersTree.search(14442) )
    # numbersTree.delete_left(92)
    # print(numbersTree.inOrderTraversal())