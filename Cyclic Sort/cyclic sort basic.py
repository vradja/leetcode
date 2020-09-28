def cyclic_sort_1(nums):
    for i, num in enumerate(nums):
        while num != i + 1:
            nums[num - 1], nums[i] = num, nums[num - 1]
            num = nums[i]
    return nums


def cyclic_sort_2(nums):  # look ahead solution, but gives [0] in output
    nums = [0] + nums
    for i, num in enumerate(nums):
        while num != nums[i]:  # If already in place
            nums[num], nums[i] = num, nums[num]
            num = nums[i]
    return nums


def cyclic_sort(nums):
    for i, num in enumerate(nums):
        while num != nums[ num - 1]: # Look ahead and skip if already in place
            nums[num - 1], nums[i] = num, nums[num - 1]
            num = nums[i]
    return nums


def main():
    print(cyclic_sort([3, 1, 5, 4, 2]))
    print(cyclic_sort([2, 6, 4, 3, 1, 5]))
    print(cyclic_sort([1, 5, 6, 4, 3, 2]))


main()
