# https://www.geeksforgeeks.org/print-k-sum-paths-binary-tree/

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


def printKSumPath(node ,  k , path =[]):
    if not node:
        return

    path.append(node.data)

    # check path in left subtree
    printKSumPath(node.left , k , path)

    # check path in right subtree
    printKSumPath(node.right , k , path)

    f = 0
    for j in range(len(path) - 1, -1, -1):
        f += path[j]
 
        # If path sum is k, print the path
        if (f == k):
            printPath(path, j)

    path.pop()


def printPath(path, i):
    for j in range(i, len(path)):
        print(path[j], end=" ")
    print()
 
    



root = Node(1)
root.left = Node(3)
root.left.left = Node(2)
root.left.right = Node(1)
root.left.right.left = Node(1)
root.right = Node(-1)
root.right.left = Node(4)
root.right.left.left = Node(1)
root.right.left.right = Node(2)
root.right.right = Node(5)
root.right.right.right =Node(2)


k = 5
printKSumPath(root, k)