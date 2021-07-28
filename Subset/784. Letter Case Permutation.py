def find_letter_case_string_permutations_1(str):  # Easy to understand solution
    permutations = [[]]
    for char in str:
        prev_level = permutations.copy()
        permutations.clear()
        for permutation in prev_level:
            permutations.append(permutation[:] + [char])
            if char.isalpha():
                permutations.append(permutation[:] + [char.swapcase()])
    return ["".join(permutation) for permutation in permutations]
    # return map("".join, permutations) # this is a bit slower but works well.


def find_letter_case_string_permutations(str):  # concsice solution
    permutations = [[]]
    for char in str:
        # the reference will be maintained. Just this snapshot of the list is iterated.
        for permutation in permutations[:]:  # calculates this list only once.
            if char.isalpha():
                permutations.append(permutation + [char.swapcase()])
            permutation.append(char)

    return ["".join(permutation) for permutation in permutations]


def main():
    print("String permutations are: " +
          str(find_letter_case_string_permutations("ad52")))
    print("String permutations are: " +
          str(find_letter_case_string_permutations("ab7c")))


main()
