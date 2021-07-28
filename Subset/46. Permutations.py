def find_permutations(nums):  # Best solution and also the fastest
    permutations = [[]]
    for num in nums:
        prev_level = permutations.copy()
        permutations.clear()
        for permutation in prev_level:  # take each permutation at previous level of nums
            for j in range(len(permutation) + 1):  # insert at each location of that permutation.
                permutations.append(permutation[j:] + [num] + permutation[:j])

    return permutations


def main():
    print("Here are all the permutations: " + str(find_permutations([1, 3, 5])))


main()
