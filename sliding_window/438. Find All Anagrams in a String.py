from collections import Counter


def update_window_counter(window_counter, new_window_end_char, window_start_char):
    window_counter[new_window_end_char] += 1
    window_counter[window_start_char] -= 1
    # if window_counter[window_start_char] == 0:
    #     del window_counter[window_start_char]
    window_counter += Counter()
    # this resets the counter by removing 0s and negatives.
    # Since this iterates over the dict, this takes a bit more time.

    # We can also use the below code snippet
    # from itertools import dropwhile
    # for key, count in dropwhile(lambda key_count: key_count[1] > 0, window_counter.most_common()):
    #     del window_counter[key]

    # window_counter = {x: y for x, y in window_counter.items() if y != 0}


def find_string_anagrams_1(string, pattern):
    result_indexes = []
    pattern_counter = Counter(pattern)
    window_counter = Counter(string[:len(pattern)])

    if pattern_counter == window_counter:
        result_indexes.append(0)

    for window_start, window_end_char in enumerate(string[len(pattern):]):
        window_start_char = string[window_start]
        update_window_counter(window_counter, window_end_char, window_start_char)

        if pattern_counter == window_counter:
            result_indexes.append(window_start + 1)

    return result_indexes


def find_string_anagrams_2(string: str, pattern: str):
    result_indexes = []

    pattern_counter = Counter(pattern)
    window_counter = Counter(string[:len(pattern)])

    if pattern_counter == window_counter:
        result_indexes.append(0)

    for window_start, window_end_char in enumerate(string[len(pattern):]):
        window_counter = Counter(string[window_start + 1:window_start + len(pattern) + 1])
        # Very slow solution since we load Counter again.

        if pattern_counter == window_counter:
            result_indexes.append(window_start + 1)

    return result_indexes


def find_string_anagrams(string: str, pattern: str):
    result_indexes = []
    matched = 0
    pattern_counter = Counter(pattern)

    for value in string[:len(pattern)]:
        if value in pattern_counter:
            pattern_counter[value] -= 1
            if pattern_counter[value] == 0:
                matched += 1

    if matched == len(pattern_counter):
        result_indexes.append(0)

    for window_start, window_end_char in enumerate(string[len(pattern):]):
        if window_end_char in pattern_counter:
            pattern_counter[window_end_char] -= 1
            if pattern_counter[window_end_char] == 0:
                matched += 1

        window_start_char = string[window_start]
        if window_start_char in pattern_counter:
            if pattern_counter[window_start_char] == 0:
                matched -= 1
            pattern_counter[window_start_char] += 1

        if matched == len(pattern_counter):
            result_indexes.append(window_start + 1)

    return result_indexes


def main():
    # print(find_string_anagrams('ppqp', 'pq'))
    # print(find_string_anagrams('baa', 'aa'))
    print(find_string_anagrams('abbcabc', 'abc'))


main()
