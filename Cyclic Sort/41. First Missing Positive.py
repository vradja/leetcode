def find_first_missing_positive_1(nums):
    i, n = 0, len(nums)
    while i < n:
        j = nums[i] - 1
        if 0 < nums[i] <= n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]  # swap
        else:
            i += 1

    for i in range(n):
        if nums[i] != i + 1:
            return i + 1

    return len(nums) + 1


def find_first_missing_positive_2(nums):
    nums = [0] + nums
    for i, num in enumerate(nums):
        while 0 < num < len(nums) and num != nums[num]:
            nums[num], num = num, nums[num]

    for i, num in enumerate(nums):
        if num != i:
            return i
    return len(nums)


def find_first_missing_positive(nums): # without modifying and using no extra space
    for i, num in enumerate(nums):
        while 0 < num <= len(nums) and num != nums[num - 1]:
            nums[num - 1], num = num, nums[num-1]

    for i, num in enumerate(nums):
        if num != i + 1:
            return i + 1
    return len(nums) + 1


def main():
    print(find_first_missing_positive([-3, 1, 5, 4, 2]))
    print(find_first_missing_positive([3, -2, 0, 1, 2]))
    print(find_first_missing_positive([3, 2, 5, 1]))


main()
