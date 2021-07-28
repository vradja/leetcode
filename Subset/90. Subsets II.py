def find_subsets(nums):
    subsets = [[]]
    nums.sort()
    prev_end = 0  # this is zero before the first element is iterated.

    for index, num in enumerate(nums):

        if prev_end and num == nums[index - 1]:  # if current element is duplicate
            start = prev_end  # assign previous end to start. Only newly added values will be copied.
        else:
            start = 0  # reset the start if no duplicate

        prev_end = len(subsets)  # find the end of previous number before the duplicate.
        # [1,2,4,4] -> find end of 2 subset. This will give end of 2 before executing 1st 4 and it can be used
        # before executing 2nd 4.

        subsets += [subset + [num] for subset in subsets[start:]]

    return subsets


def main():
    print("Here is the list of subsets: " + str(find_subsets([1, 3, 3])))
    # print("Here is the list of subsets: " + str(find_subsets([1, 5, 3, 3])))


main()
