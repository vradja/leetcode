def find_missing_numbers_1(nums):  # always index + 1 and Value -1 in subscript
    for i, num in enumerate(nums):
        while num != i + 1 and num != nums[num - 1]:  # ignore duplicated with num != nums[num - 1]
            nums[num - 1], nums[i] = num, nums[num - 1]
            num = nums[i]

    missing = list()
    for i, num in enumerate(nums):
        if num != i + 1:
            missing.append(i + 1)

    return missing


def find_missing_numbers(nums):  # Better Solution
    nums = [0] + nums
    for i, num in enumerate(nums):
        while num != i and num != nums[num]:  # Ignore Duplicates
            nums[num], nums[i] = num, nums[num]
            num = nums[i]

    return [index for index, num in enumerate(nums) if index != num]  # Get index for missing


# Using negative flips for the index containing the number
def find_missing_numbers_2(nums):
    for num in nums:
        # nums[abs(num) - 1] = abs(nums[abs(num) - 1]) * -1
        nums[abs(num) - 1] = -abs(nums[abs(num) - 1])

    missing = list()
    for i, num in enumerate(nums):
        if num > 0:
            missing.append(i + 1)

    # return [i + 1 for i in range(len(nums)) if nums[i] > 0]

    return missing


# Solution 3 with easy index 0 fix.
def find_missing_numbers_4(nums):
    nums = [0] + nums  # important step to make index -1 simpler.
    for num in nums:
        nums[abs(num)] = -abs(nums[abs(num)])  # do not forget abs for all subscripts and assigning

    return [index for index, num in enumerate(nums) if num > 0]


def find_missing_numbers_5(self, nums):  # Set solution
    return list(set(range(1, len(nums) + 1)) - set(nums))


def main():
    # print(find_missing_numbers([2, 3, 1, 8, 2, 3, 5, 1]))
    # print(find_missing_numbers([2, 4, 1, 2]))
    # print(find_missing_numbers([2, 3, 2, 1]))
    # print(find_missing_numbers([4,3,2,7,8,2,3,1]))
    print(find_missing_numbers([2, 3, 4, 5, 6, 7, 8, 1]))


main()
