from __future__ import print_function

from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def tree_right_view(root):
    right_view = list()
    queue = deque() if not root else deque([root])
    while queue:
        item = None  # after for loop, this item will store the last element of level
        for _ in range(len(queue)):
            item = queue.popleft()  # Pop left is important
            if item.left:
                queue.append(item.left)
            if item.right:
                queue.append(item.right)
        if item:
            right_view.append(item)
    return right_view


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.left.left.left = TreeNode(3)
    result = tree_right_view(root)
    print("Tree right view: ")
    for node in result:
        print(str(node.val) + " ", end='')


main()
