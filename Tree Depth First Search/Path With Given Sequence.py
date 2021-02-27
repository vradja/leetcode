class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_path(root, sequence, tree_level=0):
    if not root:
        return len(sequence) == 0
    elif tree_level > len(sequence):  # Other scenario where len(sequence) > tree_level if leaf is reached.
        return False
    elif root.val != sequence[tree_level]: # do not repeat for leaf node
        return False
    elif not root.left and not root.right:
        return tree_level == len(sequence) - 1
    else:
        # Success scenario: Sequence Number Matched with tree level.
        pass

    return find_path(root.left, sequence, tree_level + 1) or find_path(root.right, sequence, tree_level + 1)


def main():
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)

    print("Tree has path sequence: " + str(find_path(root, [1, 0, 7])))
    print("Tree has path sequence: " + str(find_path(root, [1, 1, 6])))


main()
