class node:

    def __init__(self, value):
        self.val = val
        self.left = None
        self.right = None


class BST_Operations:

    def __init__(self):
        pass

    def in_order(self, root):
        if root != None:
            self.in_order(root.left)
            print(root.val)
            self.in_order(root.right)

    def pre_order(self, root):
        if root != None:
            print(root.val)
            self.pre_order(root.left)
            self.pre_order(root.right)

    def post_order(self, root):
        if root != None:
            self.post_order(root.left)
            self.post_order(root.right)
            print(root.val)

    def tree_search(self, root, value):
        if root or root.val == value:
            return root
        elif value < root.val:
            return tree_search(root.left, value)
        else:
            return tree_search(root.right, value)

    def tree_search_iterative(self, root, value):
        temp = root

        while root or root.val == value:
            if value < root.val:
                root = root.left
            else:
                root = root.right

        return root

    def tree_min(self, root):
        while root.left:
            root = root.left
        return root

    def tree_max(self, root):
        while root.right:
            root = root.right
        return root

    def successor(self, n):
        if n.right != None:
            return self.tree_min(n.right)
        temp = n.parent
        while temp != None and n == temp.right:
            n = temp
            temp = temp.parent
        return temp

    def predccessor(self, n):
        if n.left != None:
            return self.tree_max(n.left)
        temp = n.parent
        while temp != None and n == temp.left:
            n = temp
            temp = temp.parent
        return temp

    def 
