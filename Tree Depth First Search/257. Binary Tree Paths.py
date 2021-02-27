class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def binaryTreePaths(root):
    if not root:
        return []

    if not root.left and not root.right:
        # return [str(root.val)] # Just a list will do for arrows
        return [[root.val]]  # Need list of list for flattened list

    # left = [[root.val] + path for path in binaryTreePaths(root.left)]
    # right = [[root.val] + path for path in binaryTreePaths(root.right)]

    # left = [str(root.val) + "->" + path for path in binaryTreePaths(root.left)]
    # right = [str(root.val) + "->" + path for path in binaryTreePaths(root.right)]

    # return left + right

    left_right = binaryTreePaths(root.left) + binaryTreePaths(root.right)

    # return [str(root.val) + "->" + path for path in left_right]
    return [[root.val] + path for path in left_right]


def binaryTreePaths_1(root):
    allPaths = list()
    recursive_find__all_paths(root, [], allPaths)
    return allPaths


def recursive_find__all_paths(root, current_path, allPaths):
    if not root:
        return

    current_path.append(root.val)

    if not root.left and not root.right:
        # allPaths.append(list(current_path))
        allPaths.append(str('->'.join(map(str, current_path))))  # USE JOIN and MAP for LEETCODE to Show with Arrow
    else:  # else here is an overkill, but it prevents making an another call unnecessarily.
        recursive_find__all_paths(root.left, current_path, allPaths)
        recursive_find__all_paths(root.right, current_path, allPaths)

    current_path.pop()


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("All Tree paths " +
          ": " + str(binaryTreePaths(root)))


main()
