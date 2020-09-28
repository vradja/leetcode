def find_missing_number(nums):
    for i, num in enumerate(nums):
        while num != i and num < len(nums): # here array is missing one number and hence list out of bound will happen
            nums[num], nums[i] = num, nums[num]
            num = nums[i]
    for i, num in enumerate(nums):
        if num != i:
            return i

    return len(nums)  # if all numbs are sorted, then return the last index.


def main():
    print(find_missing_number([4, 0, 3, 1]))
    print(find_missing_number([8, 3, 5, 2, 4, 6, 0, 1]))

main()