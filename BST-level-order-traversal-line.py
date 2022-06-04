# https://www.geeksforgeeks.org/print-level-order-traversal-line-line/

class newNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

    def printLevelOrderBST(self):
        queue = []

        if self is None:
            return
        
        queue.append(self)

        while queue:
            qSize = len(queue)

            while qSize > 0:
                
                temp = queue.pop(0)
                print(temp.val , end=" ")
                if(temp.left):
                    queue.append(temp.left)
                if(temp.right):
                    queue.append(temp.right)
                qSize -= 1
                # print(qSize)
            print() 
                
    

root = newNode(1)
root.left = newNode(2)
root.right = newNode(3)
root.left.left = newNode(4)
root.left.right = newNode(5)
root.right.right = newNode(6)
 
root.printLevelOrderBST();