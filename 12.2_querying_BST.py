class Node:
	def  __init__(self):
		self.parent = None
		self.key = None
		self.left = None
		self.right = None

def tree_search(node, k):
	if node.key == None or k == node.key:
		return node
	elif k < node.key:
		return tree_search(node.left, k)
	else:
		return tree_search(node.right, k)

def iterative_search(node, k):
	while node.key != None and k != node.key:
		if k < node.key:
			node = node.left
		else:
			node = node.right

	return node

def tree_minimum(node):
	while node.left:
		node = node.left
	return node

def tree_maximum(node):
	while node.right:
		node = node.right
	return node

def tree_successor(node):
	if node.right:
		return tree_minimum(node.left)
	temp_parent = node.parent
	while temp_parent and node == temp_parent.right:
		node = temp_parent
		temp_parent = temp_parent.parent
	return temp_parent

def tree_predecessor(node):
	if node.left:
		return tree_maximum(node.right)
	temp_parent = node.parent
	while temp_parent and node == temp_parent.left:
		node = temp_parent
		temp_parent = temp_parent.parent
	return temp_parent
