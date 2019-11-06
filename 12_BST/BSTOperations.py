from collections import deque


def in_order_recursive(root):
    if root != None:
        in_order(root.left)
        print(root.val)
        in_order(root.right)


def pre_order_recursive(root):
    if root != None:
        print(root.val)
        pre_order(root.left)
        pre_order(root.right)


def post_order_recursive(root):
    if root != None:
        post_order(root.left)
        post_order(root.right)
        print(root.val)


def in_order(root):
    if root == None:
        return root
    s = []
    while len(s) or root != None:
        if (root != None):
            s.append(root)
            root = root.left
        else:
            root = s.pop()
            print(root.val)
            root = root.right


def pre_order(root):
    if root == None:
        return root

    s = []
    s.append(root)
    while len(s):
        root = s.pop()
        print(root.val)
        if root.right != None:
            s.append(root.right)
        if root.left != None:
            s.append(root.left)


def post_order(root):
    if root == None:
        return root
    emp_stack = []
    out_stack = []

    emp_stack.append(root)
    while len(emp_stack):
        root = emp_stack.pop()
        out_stack.append(root)

        if root.left != None:
            emp_stack.append(root.left)
        if root.right != None:
            emp_stack.append(root.right)

    while len(out_stack):
        root = out_stack.pop()
        print(root.val)


def level_order(root):
    if root == None:
        return root

    Q = deque()
    Q.append(root)
    while len(Q):
        root = Q.popleft()
        print(root.val)
        if root.left != None:
            Q.append(root.left)
        if root.right != None:
            Q.append(root.right)


def tree_search_recursive(root, value):
    if root or root.val == value:
        return root
    elif value < root.val:
        return tree_search(root.left, value)
    else:
        return tree_search(root.right, value)


def tree_search(root, value):
    temp = root

    while root or root.val == value:
        if value < root.val:
            root = root.left
        else:
            root = root.right

    return root


def tree_min(root):
    while root.left:
        root = root.left
    return root


def tree_max(root):
    while root.right:
        root = root.right
    return root


def successor(n):
    if n.right != None:
        return tree_min(n.right)
    temp = n.parent
    while temp != None and n == temp.right:
        n = temp
        temp = temp.parent
    return temp


def predccessor(n):
    if n.left != None:
        return tree_max(n.left)
    temp = n.parent
    while temp != None and n == temp.left:
        n = temp
        temp = temp.parent
    return temp


def tree_insert(z, T=None):
    z_temp_parent = None
    temp_root = T

    while temp_root != None:
        z_temp_parent = temp_root

        if z.val < temp_root.val:
            temp_root = temp_root.left
        else:
            temp_root = temp_root.right

    z.parent = z_temp_parent

    if z_temp_parent == None:
        T = z
    elif z.val < z_temp_parent.val:
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
    # if the grand_child does have/contain some val or val which means it's not
    # None then the val it'll change the parent of the grand_child to the
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
    # if node doesn't has any left node then we'll transplant it with the
    # right child
    if node.left == None:
        transplant(root, node, node.right)
    # case 2
    # if node doesn't has any right node then we'll transplant it with the
    # left child
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
        replacement_node = tree_min(node.right)
    # case 4
    # if the successesor is not the direct and successesor is not the leaf
    # which means the successesor is a node from the middle of the right subtree
    # which does has it's own right subtree, then the following code will transplant it
    # with the child of given node, which means it'll make it the direct child of given
    # node, then it'll replace the given node by the replacement node
        if replacement_node.parent != node:
            transplant(root, replacement_node,
                       replacement_node.right)
            replacement_node.right = node.right
            replacement_node.right.parent = replacement_node

        transplant(root, node, replacement_node)
        replacement_node.left = node.left
        replacement_node.left.parent = replacement_node

def max_tree_height(root):
    if root == None:
        return 0
    left = max_height(root.left)
    right = max_height(root.right)

    return max(left, right)+1


def min_tree_height(root):
    if root == None:
        return 0
    left = max_height(root.left)
    right = max_height(root.right)

    return min(left, right)+1