from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def traverse_1(root):
    if not root:  # Important Base condition. Do not miss this.
        return list()

    list_of_levels, queue = list(), deque([root, ])
    while queue:
        level_list = list()
        for _ in range(len(queue)):
            item = queue.popleft()  # Pop left is important
            level_list.append(item.val)
            if item.left:
                queue.append(item.left)
            if item.right:
                queue.append(item.right)
        list_of_levels.append(level_list)
    return list_of_levels


def traverse_2(root):  # solution without using temporary list
    list_of_levels, level = list(), 0
    queue = deque() if not root else deque([root, ])

    while queue:
        list_of_levels.append(list())
        for _ in range(len(queue)):
            item = queue.popleft()  # Pop left is important
            list_of_levels[level].append(item.val)
            if item.left:
                queue.append(item.left)
            if item.right:
                queue.append(item.right)
        level += 1

    return list_of_levels


def traverse(root):
    list_of_levels = list()
    queue = deque() if not root else deque([root])
    while queue:
        level_list = list()
        for _ in range(len(queue)):
            item = queue.popleft()  # Pop left is important
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
