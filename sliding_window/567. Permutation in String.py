import collections, copy


def find_permutation_1(str, pattern):
    pattern_dict, window_start, matched = collections.Counter(), 0, 0

    for value in pattern:
        pattern_dict[value] += 1
        # pattern_dict[value] = pattern_dict.get(value, 0) + 1     # OR Do this

    for value in str[:len(pattern)]:
        if value in pattern_dict:
            pattern_dict[value] -= 1
            if pattern_dict[value] == 0:
                matched += 1

        if len(pattern_dict) == matched:
            return True

    for value in str[len(pattern):]:
        if value in pattern_dict:
            pattern_dict[value] -= 1
            if pattern_dict[value] == 0:
                matched += 1

        window_start_char = str[window_start]
        if window_start_char in pattern_dict:
            if pattern_dict[window_start_char] == 0:
                matched -= 1
            pattern_dict[window_start_char] += 1

        window_start += 1

        if len(pattern_dict) == matched:
            return True

    return False


def find_permutation(string, pattern):
    pattern_counter = collections.Counter(pattern)
    window_counter = collections.Counter(string[:len(pattern)])

    if window_counter == pattern_counter:
        return True

    # we dont need sliding window size, since this is a fixed size. Also no need for window_end, since all we need in value
    for window_start, value in enumerate(string[len(pattern):]):
        window_counter[value] += 1

        window_start_char = string[window_start]
        window_counter[window_start_char] -= 1
        # if window_counter[window_start_char] == 0:
        #     del window_counter[window_start_char]
        # OR
        window_counter += collections.Counter()

        if window_counter == pattern_counter:
            return True

    return False
    # return window_counter == pattern_counter # Do this only when the exit condition is done at front


def find_permutation_3(string, pattern):
    pattern_counter, matched = collections.Counter(pattern), 0

    # Iterating first half for a fixed length to see if this matches the pattern
    for value in string[:len(pattern)]:
        if value in pattern_counter:
            pattern_counter[value] -= 1
            if pattern_counter[value] == 0:
                matched += 1

        if len(pattern_counter) == matched:
            return True

    # Iterating second half
    for window_start, value in enumerate(string[len(pattern):]):
        # add the value to the window and check for matched
        if value in pattern_counter:
            pattern_counter[value] -= 1
            if pattern_counter[value] == 0:
                matched += 1

        # delete the value from the window and matched again in case the value in pattern is removed from window.
        # hence increase the pattern counter.
        window_start_char = string[window_start]

        if window_start_char in pattern_counter:
            if pattern_counter[window_start_char] == 0:
                matched -= 1
            pattern_counter[window_start_char] += 1

        if len(pattern_counter) == matched:
            return True

    return False


def main():
    # print(find_permutation("dcda", "adc"))
    print(find_permutation('oidbcaf', 'abc'))


main()
