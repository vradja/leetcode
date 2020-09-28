def find_all_duplicates_1(nums):  # Ditto copy of LC 448
    nums = [0] + nums
    for i, num in enumerate(nums):
        while num != i and num != nums[num]:
            nums[num], nums[i] = num, nums[num]
            num = nums[i]

    return [num for index, num in enumerate(nums) if
            index != num]  # get the value for duplicates and get index for missing.


def find_all_duplicates(self, nums):  # Look Ahead Solution
    nums = [0] + nums
    for i, num in enumerate(nums):
        while num != nums[num]:  # Look ahead and ignore duplicates or already in place
            nums[num], nums[i] = num, nums[num]
            num = nums[i]

    return [num for index, num in enumerate(nums) if
            index != num]  # get the value for duplicates and get index for missing.


# with flips
def find_all_duplicates_3(nums):
    nums = [0] + nums  # important step to make index -1 simpler.
    duplicates = list()
    for num in nums:
        if nums[abs(num)] < 0:  # For finding duplicates, this should come here instead of at the end.
            duplicates.append(abs(num))
        else:
            nums[abs(num)] = -abs(nums[abs(num)])  # do not forget abs for all subscripts and assigning

    return duplicates


def main():
    print(find_all_duplicates([4, 3, 2, 7, 8, 2, 3, 1]))
    print(find_all_duplicates([3, 4, 4, 5, 5]))
    print(find_all_duplicates([5, 4, 7, 2, 3, 5, 3]))


main()
