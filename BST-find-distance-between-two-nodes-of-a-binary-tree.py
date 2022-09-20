# https://www.geeksforgeeks.org/find-distance-between-two-nodes-of-a-binary-tree/


"""
A python program to find distance between n1
and n2 in binary tree
"""
# binary tree node


class Node:
	# Constructor to create new node
	def __init__(self, data):
		self.data = data
		self.left = self.right = None


# This function returns pointer to LCA of
# two given values n1 and n2.
def find_least_common_ancestor(root: Node, n1: int, n2: int) -> Node:
    # Base case
   
    if root is None:
        return root
    print(root.data)
    # If either n1 or n2 matches with root's
    # key, report the presence by returning root
    if root.data == n1 or root.data == n2:
        return root
    # Look for keys in left and right subtrees
    left = find_least_common_ancestor(root.left, n1, n2)
    right = find_least_common_ancestor(root.right, n1, n2)
    if left and right:
        return root
    # Otherwise check if left subtree or
    # right subtree is Least Common Ancestor
    if left:
        return left
    else:
        return right
# function to find distance of any node
# from root



def find_distance_from_ancestor_node(root: Node, data: int) -> int:
	# case when we reach a beyond leaf node
	# or when tree is empty
	if root is None:
		return -1
	# Node is found then return 0
	if root.data == data:
		return 0

	left = find_distance_from_ancestor_node(root.left, data)
	right = find_distance_from_ancestor_node(root.right, data)
	distance = max(left, right)
	return distance+1 if distance >= 0 else -1

# function to find distance between two
# nodes in a binary tree


def find_distance_between_two_nodes(root: Node, n1: int, n2: int):

	lca = find_least_common_ancestor(root, n1, n2)

	return find_distance_from_ancestor_node(lca, n1) + find_distance_from_ancestor_node(lca, n2) if lca else -1


# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.right = Node(8)


print(find_least_common_ancestor(root,4,7).data)

# print("Dist(4,5) = ", find_distance_between_two_nodes(root, 4, 5))
# print("Dist(4,6) = ", find_distance_between_two_nodes(root, 4, 6))
# print("Dist(3,4) = ", find_distance_between_two_nodes(root, 3, 4))
# print("Dist(2,4) = ", find_distance_between_two_nodes(root, 2, 4))
# print("Dist(8,5) = ", find_distance_between_two_nodes(root, 8, 5))

# This article is contributed by Shweta Singh.
# This article is improved by Sreeramachandra
