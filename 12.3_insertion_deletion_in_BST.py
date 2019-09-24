class Node:
	def  __init__(self):
		self.parent = None
		self.cost = None
		self.left = None
		self.right = None

def tree_insert(T=None, z):
	z_temp_parent = None
	temp_root = T

	while temp_root != None:
		z_temp_parent = temp_root
    
		if z.key < temp_root.key:
			temp_root = temp_root.left
		else:
			temp_root = temp_root.right

	z.parent = z_temp_parent

	if z_temp_parent == None:
		T = z
	elif z.key < z_temp_parent:
		z_temp_parent.left = z 
	else:
		z_temp_parent.right = z


def transplant(root, child, grand_child):
  # base case if the root node doesn't has any parent
  # which means the root is the root of the tree
  # then the grand_child will be the root
  if child.parent == None:
    oot = grand_child

  # if the given root_node is the left child of the parent
  # then the parent will point to the right child
  elif child == child.parent.left:
    child.parent.left = grand_child
  else:
  # if the given root_node is the right child of the parent
  # then the parent will point to the left child
    child.parent.right = grand_child
  # if the grand_child does have/contain some value or key which means it's not
  # None then the value it'll change the parent of the grand_child to the
  # parent of child 
  if grand_child != None:
    grand_child.parent = child.parent


def tree_delete(root, node):
  """
  deleting a node in bst has some rules. 
  * if there is a successor in the childs of given node then it should be replaced with that
  the following cases can be happen while deleting a node
  """
  # case 1
  # if node doesn't has any left node then we'll transplant it with the right child
	if node.left == None:
		transplant(root, node, node.right)
  # case 2
  # if node doesn't has any right node then we'll transplant it with the left child
	elif node.right == None:
		transplant(root, node, node.left)
	else:
    # case 3
    # if the successesor is direct child of the given node or
    # some child which doesn't has any left node but contains the right nodes
    # so the right subtree will be greater then the replacement node which means the 
    # successesor will be the the replacement node, then we'll replace it with that
    # so the algorithm will find successesor on line 75 then jump to line 87 and will 
    # transplant child node with the given node
		replacement_node = tree_minimum(node.right)
    # case 4
    # if the successesor is not the direct and successesor is not the leaf
    # which means the successesor is a node from the middle of the right subtree
    # which does has it's own right subtree, then the following code will transplant it
    # with the child of given node, which means it'll make it the direct child of given
    # node, then it'll replace the given node by the replacement node 
		if replacement_node.parent != node:
			transplant(root, replacement_node, replacement_node.right)
			replacement_node.right = node.right
			replacement_node.right.parent = replacement_node

		transplant(root, node, replacement_node)
		replacement_node.left = node.left
		replacement_node.left.parent = replacement_node
