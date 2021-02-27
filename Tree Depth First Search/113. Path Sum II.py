class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def recursive_find_paths(root, sum, current_path, allPaths):
    if not root:
        return

    current_path.append(root.val)

    if not root.left and not root.right and root.val == sum:
        allPaths.append(list(current_path))  # create an another list object to append, since current_path is changing
    else:
        recursive_find_paths(root.left, sum - root.val, current_path, allPaths)
        recursive_find_paths(root.right, sum - root.val, current_path, allPaths)

    current_path.pop()  # Backtracking: do this to remove unsuccessful nodes or to backtrack from successful ones.


def find_paths_1(root, sum):
    allPaths = list()
    recursive_find_paths(root, sum, [], allPaths)
    return allPaths


# Beautiful solution just using one function
def find_paths(root, sum):
    if not root:
        return []

    if not root.left and not root.right and sum == root.val:
        return [[root.val]]

    left_right = find_paths(root.left, sum - root.val) + find_paths(root.right, sum - root.val)

    return [[root.val] + path for path in left_right]


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    sum = 23
    print("Tree paths with sum " + str(sum) +
          ": " + str(find_paths(root, sum)))


main()
