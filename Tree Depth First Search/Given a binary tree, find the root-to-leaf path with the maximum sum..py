class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def binaryTreeMaxPaths(root):
    if not root:
        return []

    if not root.left and not root.right:
        return [{'path': [root.val], 'max_value': root.val}]  # need dictionary to create a max at each leaf level

    left_right = binaryTreeMaxPaths(root.left) + binaryTreeMaxPaths(root.right)

    return [{'path': [root.val] + path['path'], 'max_value': path['max_value'] + root.val} for path in left_right]


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(15)
    print("All Tree paths " +
          ": " + str(max(binaryTreeMaxPaths(root), key=lambda x: x['max_value'])['path']))
    # USE LAMBDA ABOVE


main()
