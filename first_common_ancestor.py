"""
Design an algorithm and write code to find the first common ancestor
of two nodes in a binary tree. Avoid storing additional nodes in a data
structure. NOTE: This is not necessarily a binary search tree.
"""

#solution1
def common_ancestor(root, p, q):
	if not cover(root, p) or not cover(root, q):
		return None
	elif cover(p, q):
		return p
	elif cover(q, p):
		return q
	
	sibling = get_sibling(p)
	parent = p.parent
	while not cover(sibling, q):
		sibling = get_sibling(parent)
		parent = parent.parent

	return parent


def cover(root, p):
	if not root:
		return False
	if root == p:
		return True

	return cover(root.right, p) or cover(root.left, p)

def get_sibling(node):
	if not node or not node.parent:
		return None
	parent = node.parent
	return parent.right if parent.left == node else parent.left 


#solution2
def common_ancestor(p, q):
	delta = depth(p) - depth(q)
	first = q if delta > 0 else p
	second = p if delta > 0 else q
	second = go_up(second, delta)

	while first != second and first is not None and second is not None:
		first = first.parent
		second = second.parent
	return first if first == second else None 

def go_up(node, delta):
	while node and delta > 0:
		node = node.parent
		delta -= 1
	return node


def depth(node):
	depth = 0
	while node:
		node = node.parent
		depth += 1
	return depth






