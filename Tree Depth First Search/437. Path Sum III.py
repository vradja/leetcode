class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


total_paths = 0


# Brute Force Method
def count_paths_1(root, S):
    recursive_dfs(root, S)
    return total_paths


def recursive_dfs(root, S):
    if not root:
        return
    check_sum(root, S)
    recursive_dfs(root.left, S)
    recursive_dfs(root.right, S)


def check_sum(root, target):
    if not root:
        return
    elif root.val == target:
        global total_paths
        total_paths += 1
    check_sum(root.left, target - root.val)
    check_sum(root.right, target - root.val)


# Optimized prefix Sum Method
def count_paths(root, S):
    cache = {0: 1}
    dfs(root, S, 0, cache)
    return total_paths


def dfs(root, target, currPathSum, cache):
    # exit condition
    if root is None:
        return

    # calculate currPathSum and required oldPathSum
    currPathSum += root.val
    oldPathSum = currPathSum - target

    # update result and cache
    global total_paths
    total_paths += cache.get(oldPathSum, 0)
    cache[currPathSum] = cache.get(currPathSum, 0) + 1

    # dfs breakdown
    dfs(root.left, target, currPathSum, cache)
    dfs(root.right, target, currPathSum, cache)

    # Backtracking
    # when move to a different branch, the currPathSum is no longer available, hence remove one.
    cache[currPathSum] -= 1 # DO NOT DELETE. If count is 2, we may end up deleting the entry


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree has paths: " + str(count_paths(root, 11)))


main()
