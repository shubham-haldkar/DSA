# https://www.geeksforgeeks.org/print-unique-rows/

class BinaryTree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def addNode(self,data):
        if not self.data:
            self.data = data
        if data == self.data:
            return
        if(data < self.data):
            if  self.left:
                self.left.addNode(data)
            else:
                self.left = BinaryTree(data)
        else:
            if self.right:
                self.right.addNode(data)
            else:
                self.right = BinaryTree(data)

    def inOrderTraversal(self):
        if(self.data != 0):
            convertToBinary(self.data)        
        if self.left:
            self.left.inOrderTraversal()       
 
        if self.right:
            self.right.inOrderTraversal()

    def printAnswer(self):
        elem = self.inOrderTraversal()
        # print(elem)
        # for i in elem:
        #     convertToBinary(i)
        #     print()
COL = 5
def convertToBinary(p):
    for i in range(COL):
        print(p % 2 ,end = " ")
        p = int(p//2)
    print("")
 


def findUniqueRows(M):
    bst = BinaryTree(None)

    for i in M:
        bst.addNode(convert(i))
    bst.printAnswer()

def convert(arr):
    ans = 0
    for j in range(len(arr)):
        ans += pow(2,j)*arr[j]
 
    return ans

M = [[0, 1, 0, 0, 1],
     [1, 0, 1, 1, 0],
     [0, 1, 0, 0, 1],
     [1, 0, 1, 0, 0]]
 
findUniqueRows(M)