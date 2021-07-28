def numTrees_1(start=1, end=1, memo={}):  # Constraints: 1 <= n <= 19
    if start >= end:  # start can be more than end due to left call. if there exist a node, it will atleast return 1
        return 1

    if (start, end) in memo:
        return memo[(start, end)]

    bst_count = 0

    for value in range(start, end + 1):
        left = numTrees(start, value - 1, memo)  # always omit the current node and find combination of left & right
        right = numTrees(value + 1, end, memo)

        bst_count += left * right  # multiple is same as for of for.

    memo[(start, end)] = bst_count

    return bst_count


# Simpler approach
def numTrees(end, memo={}):  # Optimized solution. Since count only matters here, we dont need start and end
    if end <= 1:
        return 1

    if end in memo:
        return memo[end]

    bst_count = 0

    for i in range(1, end + 1):
        left = numTrees(i - 1)
        right = numTrees(end - i)

        bst_count += left * right

    memo[end] = bst_count

    return bst_count


def main():
    print("Total trees: " + str(numTrees(end=2)))
    print("Total trees: " + str(numTrees(end=3)))


main()
