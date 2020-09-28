def find_corrupt_numbers_1(nums):
    nums = [0] + nums
    for i, num in enumerate(nums):
        while num != i and num != nums[num]:
            nums[num], nums[i] = num, nums[num]
            num = nums[i]

    return [(index, num) for index, num in enumerate(nums) if
            index != num]  # get the value for duplicates and get index for misding.

def find_corrupt_numbers(nums):
    nums = [0] + nums
    for i, num in enumerate(nums):
        while num != nums[num]:
            nums[num], nums[i] = num, nums[num]
            num = nums[i]

    return [(index, num) for index, num in enumerate(nums) if
            index != num]  # get the value for duplicates and get index for mising.

def main():
    print(find_corrupt_numbers([3, 1, 2, 5, 2]))
    print(find_corrupt_numbers([3, 1, 2, 3, 6, 4]))


main()
