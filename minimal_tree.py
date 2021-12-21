"""
Given a sorted (increased order) array with unique integer elements, 
write an algorithm to create a binary search tree with minimal height.
"""

class Node: 
	def __init__(self, item)
	self.right = None
	self.left = None
	self.val = item

def array_to_binary_tree(array, start, end):
	if start > end:
		return None
	mid = (start + end) // 2
	root = Node(array[mid])
	root.left = array_to_binary_tree(array, start, mid-1)
	root.right = array_to_binary_tree(array, mid+1, end)
	return root
