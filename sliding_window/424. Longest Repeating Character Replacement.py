import collections


def length_of_longest_substring(string, K):
    window_start, replaceable_count, longest_substring, max_freq_char_count = 0, 0, 0, 0
    freq_counter = collections.Counter()

    for window_end, value in enumerate(string):
        freq_counter[value] += 1
        max_freq_char_count = max(max_freq_char_count, freq_counter[
            value])  # Better Approach, create a sliding window and expect for higher size.
        # max_freq_char_count = freq_dict[max(freq_dict, key = lambda x: freq_dict[x])]
        # max_freq_char_count = max(freq_dict.values())
        replaceable_count = (window_end - window_start + 1) - max_freq_char_count

        if replaceable_count > K:
            freq_counter[string[window_start]] -= 1
            window_start += 1

        longest_substring = max(longest_substring, window_end - window_start + 1)

    return longest_substring


def main():
    print(length_of_longest_substring("aabcdefaaa", 2))
    # print(length_of_longest_substring("aabccbbad", 2))
    # print(length_of_longest_substring("abbcb", 1))
    # print(length_of_longest_substring("abccde", 1))


main()
