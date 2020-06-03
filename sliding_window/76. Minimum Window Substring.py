import collections


def find_substring_1(string, pattern):
    pattern_counter = collections.Counter(pattern)
    window_counter = collections.Counter()

    min_window, window_start = None, 0

    for window_end, value in enumerate(string):
        window_counter[value] += 1

        # Find substring match and then shrink from left
        while not bool(pattern_counter - window_counter):
            new_min_window = string[window_start:window_end + 1]
            if min_window is None or len(min_window) > len(new_min_window):
                min_window = new_min_window
            window_counter[string[window_start]] -= 1
            window_start += 1

    return min_window if min_window is not None else ""


def find_substring(string, pattern):
    pattern_counter = collections.Counter(pattern)
    min_window, window_start, matched = string + '!', 0, 0

    for window_end, window_end_char in enumerate(string):
        # STEP 1: Reduce count in dict
        if window_end_char in pattern_counter:
            pattern_counter[window_end_char] -= 1
            if pattern_counter[window_end_char] == 0:
                matched += 1

        # STEP 2: Find a match of substring and shrink
        while matched == len(pattern_counter):

            # STEP 3: Calculate result match substring. (Here we find minimal substring possible)
            window_matched = string[window_start: window_end + 1]
            if len(min_window) > len(window_matched):
                min_window = window_matched

            # STEP 4: Shrink the window_from left
            window_start_char = string[window_start]
            if window_start_char in pattern_counter:
                if pattern_counter[window_start_char] == 0:
                    matched -= 1
                pattern_counter[window_start_char] += 1
            window_start += 1

    return min_window if len(min_window) <= len(string) else ""


# Approach 3: using 2 value set for min_window showing start and end of sliding window
def find_substring_3(string, pattern):
    pattern_counter = collections.Counter(pattern)
    min_window, window_start, matched = (0, len(string) + 1), 0, 0

    for window_end, window_end_char in enumerate(string):
        # STEP 1: Reduce count in dict
        if window_end_char in pattern_counter:
            pattern_counter[window_end_char] -= 1
            if pattern_counter[window_end_char] == 0:
                matched += 1

        # STEP 2: Find a match of substring and shrink
        while matched == len(pattern_counter):

            # STEP 3: Calculate result match substring. (Here we find minimal substring possible)
            if min_window[1] - min_window[0] > window_end - window_start + 1:
                min_window = (window_start, window_end + 1)

            # STEP 4: Shrink the window_from left
            window_start_char = string[window_start]
            if window_start_char in pattern_counter:
                if pattern_counter[window_start_char] == 0:
                    matched -= 1
                pattern_counter[window_start_char] += 1
            window_start += 1

    return string[min_window[0]:min_window[1]] if min_window[1] - min_window[0] < len(string) + 1 else ""

# Not so good solution.
def find_substring_4(string, pattern):
    window_start, matched, substr_start = 0, 0, 0
    min_length = len(string) + 1
    pattern_counter = collections.Counter(pattern)

    # try to extend the range [window_start, window_end]
    for window_end, window_end_char in enumerate(string):
        if window_end_char in pattern_counter:
            pattern_counter[window_end_char] -= 1
            if pattern_counter[window_end_char] >= 0:  # Count every matching of a character
                matched += 1

        # Shrink the window if we can, finish as soon as we remove a matched character
        while matched == len(pattern):
            if min_length > window_end - window_start + 1:
                min_length = window_end - window_start + 1
                substr_start = window_start

            left_char = string[window_start]
            window_start += 1
            if left_char in pattern_counter:
                # Note that we could have redundant matching characters, therefore we'll decrement the
                # matched count only when a useful occurrence of a matched character is going out of the window
                if pattern_counter[left_char] == 0:
                    matched -= 1
                pattern_counter[left_char] += 1

    if min_length > len(string):
        return ""
    return string[substr_start:substr_start + min_length]


def main():
    # print(find_substring('aaabdec', 'aabc'))
    print(find_substring('aaabb', 'aab'))

main()
