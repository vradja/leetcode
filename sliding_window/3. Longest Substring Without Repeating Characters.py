# Given a string, find the length of the longest substring which has no repeating characters.


def non_repeat_substring(string):
    window_start, longest_subset = 0, 0
    index_dict = dict()

    for window_end, value in enumerate(string):
        if value in index_dict:
            window_start = max(window_start, index_dict[value] + 1)
            # Move ahead of the previous index of repeating character. # sliding window cannot contain duplicate.
        index_dict[value] = window_end
        longest_subset = max(longest_subset, window_end - window_start + 1)

    return longest_subset

def main():
    # print("Length of the longest substring: " + str(non_repeat_substring("aabccbb")))
    # print("Length of the longest substring: " + str(non_repeat_substring("abbbb")))
    # print("Length of the longest substring: " + str(non_repeat_substring("abccde")))
    # print("Length of the longest substring: " + str(non_repeat_substring("abccbad")))
    print("Length of the longest substring: " + str(non_repeat_substring("abba")))
    # print("Length of the longest substring: " + str(non_repeat_substring("abcdadc")))


main()
