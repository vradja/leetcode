def find_subsets(nums):
    subsets = [[]]
    for num in nums:
        subsets += [subset + [num] for subset in subsets]
    return subsets


def main():
    print("Here is the list of subsets: " + str(find_subsets([1, 3])))
    print("Here is the list of subsets: " + str(find_subsets([1, 5, 3])))


main()
