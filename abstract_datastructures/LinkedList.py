class Node:
    def __init__(self, value):
        self.val = value
        self.next = None

    def push(self, root, value):
        temp = root
        while temp.next:
            temp = temp.next
        temp.next = Node(value)
        return root 

    def pop(self, root):
        temp = root
        prev = None
        while temp.next:
            prev = temp
            temp = temp.next
        prev.next = None
        return root 

    def insert(self, value, root=None, index=None):
        if not root:
            return Node(value)
        elif not index:
            return push(root, value)
        i = 0
        temp = root
        while i < index-1:
            i += 1
            temp = temp.next

        b = Node(value)
        b.next = temp.next
        temp.next = b
        return root

    def print_list(self, root):
        temp = root 
        while temp:
            print(temp.val)
            temp = temp.next


    def delete(self, root, value=None, index=None):
        temp = root 
        while temp.val != value:
            temp = temp.next
        return root
