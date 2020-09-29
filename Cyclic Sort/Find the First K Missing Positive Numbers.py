def find_first_k_missing_positive_1(nums, k):
    n = len(nums)
    i = 0
    while i < len(nums):
        j = nums[i] - 1
        if 0 < nums[i] <= n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]  # swap
        else:
            i += 1

    missingNumbers = []
    extraNumbers = set()
    for i in range(n):
        if len(missingNumbers) < k:
            if nums[i] != i + 1:
                missingNumbers.append(i + 1)
                extraNumbers.add(nums[i])

    # add the remaining missing numbers
    i = 1
    while len(missingNumbers) < k:
        candidateNumber = i + n
        # ignore if the array contains the candidate number
        if candidateNumber not in extraNumbers:
            missingNumbers.append(candidateNumber)
        i += 1

    return missingNumbers


def find_first_k_missing_positive(nums, k):
    # Usual cyclic sorting
    nums = [0] + nums
    for i, num in enumerate(nums):
        while 0 < num < len(nums) and num != nums[num]:
            nums[num], nums[i] = num, nums[num]
            num = nums[i]  # IMPORTANT STEP: DO NOT FORGET

    missing_positives = list()
    extra_numbers = set()

    # Check if missing positive number is from 1 to len(nums)
    # Here K number of missing positives are reached, break!
    # Keep track of extra numbers both +ve and -ve encountered: They will be more than len(nums) or -ve numbers.
    for i, num in enumerate(nums):
        if len(missing_positives) < k:
            if num != i:
                missing_positives.append(i)
                extra_numbers.add(num)  # just keep track for Step 3 for missing positives > len(nums).
                # ONLY -VE AND +VE NUMBERS > LEN(NUMS) WILL APPEAR HERE, SINCE THEY DON'T HAVE INDEX TO BE SORTED INTO.
        else:
            break

    # Step 3: if we have iterated over 1 to len(nums) and still have not satisfied K, we need to look forward.
    # Make sure we increment one by one starting at len(nums) onwards, with len(nums) inclusive.
    next_positive_number = len(nums)
    while len(missing_positives) < k:
        if next_positive_number not in extra_numbers:
            missing_positives.append(next_positive_number)
        next_positive_number += 1

    return missing_positives


def main():
    print(find_first_k_missing_positive([3, -1, 4, 5, 5], 3))
    print(find_first_k_missing_positive([2, 3, 4], 3))
    print(find_first_k_missing_positive([-2, -3, 4], 2))


main()
