from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def traverse(root):
    list_of_levels, queue = list(), deque()
    queue.append(root)
    while queue:
        level_list = list()
        for _ in range(len(queue)):
            item = queue.popleft()
            level_list.append(item.val)
            if item.left:
                queue.append(item.left)
            if item.right:
                queue.append(item.right)
        list_of_levels.append(level_list)
    return list_of_levels


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level order traversal: " + str(traverse(root)))


main()
