def inorder_tree_walk(node):
	if node.key != None:
		inorder_tree_walk(node.left)
		print(node.key)
		inorder_tree_walk(node.right)