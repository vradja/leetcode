from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def find_successor(root, key):
    queue = deque() if not root else deque([root])
    while queue:  # No need for FOR loop to keep track of levels.
        item = queue.popleft()  # Pop left is important
        if item.left:
            queue.append(item.left)
        if item.right:
            queue.append(item.right)

        # DO this after inserting LEFT and RIGHT, so that you dont miss the next values being pushed to queue
        if item.val == key:
            break
    return queue.popleft() if queue else None


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    result = find_successor(root, 12)
    if result:
        print(result.val)
    result = find_successor(root, 9)
    if result:
        print(result.val)


main()
