import BSTOperations as operations

class Node:

    def __init__(self, value):
        self.parent = None
        self.val = value
        self.left = None
        self.right = None

def main():
    nums = [3,10,1,6,4,7,14,13,15]
    root = Node(8)
    for i in nums:
        n = Node(i)
        operations.tree_insert(n, root)
    
    # m = Node(nums[1])
    # print("in-order")
    operations.level_order(root)

    print("height: ", operations.max_tree_height(root))
    
    # operations.tree_delete(root, root.left)
    
    # print("pre-order")
    # operations.pre_order(root)
    # print("post-order")
    # operations.post_order(root)

if __name__ == '__main__':
    main()