def tree_dfs(r, s):
	if r != None:
		if r.val == s:
			return r
		tree_dfs(r.left)
		tree_dfs(r.right)
		print("false")

def dfs_recursive(node):
	

	visited_nodes = []
	if node not in visited_nodes:
		visited_nodes.appened(node)
