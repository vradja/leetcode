def fruits_into_baskets(fruits):
    window_start, longest_substring = 0, 0
    index_dict = dict()

    for window_end, fruit in enumerate(fruits):
        index_dict[fruit] = window_end

        if len(index_dict) > 2:
            window_start = min(index_dict.values())  # Needed for removing the least index character
            index_dict.pop(fruits[window_start], None)
            window_start += 1

        longest_substring = max(longest_substring, window_end - window_start + 1)

    return longest_substring


def main():
    # print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'A', 'C'])))
    # print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C'])))
    print("Maximum number of fruits: " + str(fruits_into_baskets("abaccc")))


main()
