# https://www.geeksforgeeks.org/print-nodes-top-view-binary-tree/

 

from collections import defaultdict
from email.policy import default
import queue


class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.left = None
        self.right = None
        self.hd = 0


def printTopView(node  ):
    if(node == None):
        return
    
    hd_dict = defaultdict(list)

    queue = []
    queue.append(node)
    hd = 0

    while(len(queue)):
        temp = queue.pop(0)
        hd = temp.hd
        if hd not in hd_dict:
            hd_dict[hd] = temp.data

        if(temp.left):
            temp.left.hd = hd-1
            queue.append(temp.left)
        
        if(temp.right):
            temp.right.hd = hd+1
            queue.append(temp.right)
        
    for i in hd_dict:
        print(hd_dict[i] , end=" ")

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(4)
root.left.right.right = Node(5)
root.left.right.right.right = Node(6)
print("Following are nodes in top",
      "view of Binary Tree")
printTopView(root)
 