from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def find_level_averages(root):
    avg_of_levels = list()
    queue = deque() if not root else deque([root])

    while queue:
        level_sum, queue_length = 0.0, len(queue) # Here 0.0 is needed to make level_sum DECIMAL
        for _ in range(queue_length):
            item = queue.popleft() # DO NOT MISS popLEFT
            level_sum += item.val
            if item.left:
                queue.append(item.left)
            if item.right:
                queue.append(item.right)
        avg_of_levels.append(level_sum / queue_length)

    return avg_of_levels


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level averages are: " + str(find_level_averages(root)))


main()
