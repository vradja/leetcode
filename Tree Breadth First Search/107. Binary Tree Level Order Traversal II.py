from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def traverse_1(root):  # slicing solution
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
    return list_of_levels[::-1]


def traverse(root):  # dequeue without list
    list_of_levels = deque()
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
        list_of_levels.appendleft(level_list)
    return list_of_levels


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Reverse level order traversal: " + str(traverse(root)))


main()
