class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_leaf(root): # NOT EVEN NEEDED. We can DO without this
    return True if not root.left and not root.right else False


def has_path(root, sum):
    # Recursion will eventually reaches here, if True is not reached in any path
    if not root:
        return False

    # The only condition which returns True.
    if not root.left and not root.right and root.val == sum:
        return True

    return has_path(root.left, sum - root.val) or has_path(root.right, sum - root.val)


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree has path: " + str(has_path(root, 23)))
    print("Tree has path: " + str(has_path(root, 16)))


main()
