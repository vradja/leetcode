from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def traverse_1(root):  # using slicing
    list_of_levels, flip = deque(), False
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
        if flip:
            level_list = level_list[::-1]
        list_of_levels.append(level_list)
        flip = not flip
    return list_of_levels


def traverse_2(root):  # using dequeue for flip, convert deque to list
    list_of_levels, flip = deque(), False
    queue = deque() if not root else deque([root])
    while queue:
        level_list = deque()
        for _ in range(len(queue)):
            item = queue.popleft()  # Pop left is important
            if flip:
                level_list.appendleft(item.val)
            else:
                level_list.append(item.val)

            if item.left:
                queue.append(item.left)
            if item.right:
                queue.append(item.right)
        list_of_levels.append(list(level_list))
        flip = not flip
    return list(list_of_levels)


def traverse(root):  # using dequeue for flip and NO conversion
    list_of_levels, flip = deque(), False
    queue = deque() if not root else deque([root])
    while queue:
        level_list = deque()
        for _ in range(len(queue)):
            item = queue.popleft()  # Pop left is important
            if flip:
                level_list.appendleft(item.val)
            else:
                level_list.append(item.val)

            if item.left:
                queue.append(item.left)
            if item.right:
                queue.append(item.right)
        list_of_levels.append(level_list)
        flip = not flip
    return list_of_levels


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.right.left.left = TreeNode(20)
    root.right.left.right = TreeNode(17)
    print("Zigzag traversal: " + str(traverse(root)))


main()
