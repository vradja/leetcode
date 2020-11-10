from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def find_minimum_depth_1(root):  # check if leaf node is reached
    queue = deque() if not root else deque([root])
    level = 0
    while queue:
        for _ in range(len(queue)):
            item = queue.popleft()  # DO NOT MISS popLEFT
            if not item.left and not item.right:  # If leaf Node.
                return level + 1
            if item.left:
                queue.append(item.left)
            if item.right:
                queue.append(item.right)
        level += 1
    return 0  # This will be reached only if there are NO Nodes in the tree and root == None


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree Minimum Depth: " + str(find_minimum_depth(root)))
    root.left.left = TreeNode(9)
    root.right.left.left = TreeNode(11)
    print("Tree Minimum Depth: " + str(find_minimum_depth(root)))


main()
