def fruits_into_baskets(fruits):
    window_start, longest_subset, index_dict = 0, 0, dict()

    for window_end, fruit in enumerate(fruits):
        index_dict[fruit] = window_end

        if len(index_dict) > 2:
            window_start = min(index_dict.values())  # This gets rid of the least index character.
            index_dict.pop(fruits[window_start], None)
            window_start += 1

        longest_subset = max(longest_subset, window_end - window_start + 1)

    return longest_subset


def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
    window_start, longest_subset, index_dict = 0, 0, dict()

    for window_end, value in enumerate(s):
        index_dict[value] = window_end

        if len(index_dict) > 2:
            window_start = min(index_dict.values())
            index_dict.pop(s[window_start], None)
            window_start += 1

        longest_subset = max(longest_subset, window_end - window_start + 1)

    return longest_subset


def main():
    # print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'A', 'C'])))
    # print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C'])))
    print("Maximum number of fruits: " + str(fruits_into_baskets("abaccc")))


main()
