class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_sum_of_path_numbers(root):
    return recursive_find_sum_of_path_numbers(root, 0)

# DO NOT USE left_right solution for this problem, due to 0 being present in the tree. Gets harder to keep track of its
# occurance. Better to TOP DOWN approach for this

# This is the better solution
def recursive_find_sum_of_path_numbers(root, pathSum):
    if not root:
        return 0

    # if leaf node
    if not root.left and not root.right:
        return pathSum

    pathSum = pathSum * 10 + root.val # similar to the adding prefix to the left_right

    return recursive_find_sum_of_path_numbers(root.left, pathSum) + recursive_find_sum_of_path_numbers(root.right,
                                                                                                       pathSum)

# Use the above solution.
def recursive_find_sum_of_path_numbers_1(root, pathSum):
    if not root:
        return

    pathSum = pathSum * 10 + root.val
    # if lead node
    if not root.left and not root.right:
        sum_path += pathSum

    recursive_find_sum_of_path_numbers(root.left, pathSum)
    recursive_find_sum_of_path_numbers(root.right, pathSum)


def main():
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)
    print("Total Sum of Path Numbers: " + str(find_sum_of_path_numbers(root)))


main()
