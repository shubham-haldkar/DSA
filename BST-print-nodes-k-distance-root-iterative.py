# https://www.geeksforgeeks.org/print-nodes-k-distance-root-iterative/

 

class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.left = None
        self.right = None

def printKDistanceNodes(root , distance):
    if(root == None):
        return False
    queue = []
    level  = 1
    queue.append(root)
    queue.append(None)
    test = [root.data]
 
    flag = False

    while(len(queue)):
        print(test)
        
        n = queue.pop(0)
        test.pop(0)
        
        if(n!=None and distance == level):
            print(n.data, end=" ")
            flag = True

        if(n == None):
            if(len(queue)):
                queue.append(None)
                test.append(None)
            level+=1

            if(level > distance):
                break
        else:
 
            if(n.left):
                test.append(n.left.data)
                queue.append(n.left)
            if(n.right):
                queue.append(n.right)
                test.append(n.right.data)
    return flag



root = Node(20)
root.left = Node(10)
root.right = Node(30)
root.left.left = Node(5)
root.left.right = Node(15)
root.left.right.left = Node(12)
root.right.left = Node(25)
root.right.right = Node(40)

print("data at level 1 : ", end = "")
ret = printKDistanceNodes(root, 1)
if (ret == False):
    print("Number exceeds total",
              "number of levels")
print()
print("data at level 2 : ", end = "")
ret = printKDistanceNodes(root, 2)
if (ret == False) :
    print("Number exceeds total",
              "number of levels")
print()
print("data at level 3 : ", end = "")

ret = printKDistanceNodes(root, 3)
if (ret == False) :
    print("Number exceeds total",
              "number of levels")
print()
print("data at level 6 : ", end = "")
ret = printKDistanceNodes(root, 6)
if (ret == False):
    print("Number exceeds total number of levels")
 

