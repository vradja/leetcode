from collections import Counter, OrderedDict


# Working solution but TIME EXCEEDED
def minWindow(S, T):
    min_sub_sequence = ""
    pattern_counter = Counter(T)
    pattern_first_char_indices = [i for i, ltr in enumerate(S) if ltr == T[0]]

    for first_char_index in pattern_first_char_indices:
        window_start = first_char_index
        matched_till_index = -1
        for window_end in range(first_char_index, len(S)):
            window_end_char = S[window_end]

            if window_end_char in pattern_counter:
                if matched_till_index < len(T) - 1:
                    if window_end_char == T[matched_till_index + 1]:
                        matched_till_index += 1
                    else:
                        if window_end_char in T[:matched_till_index + 1]:
                            # this is duplicate, so continue
                            continue
                else:
                    break
            else:
                continue

            if matched_till_index == len(T) - 1:
                if not min_sub_sequence or len(min_sub_sequence) > window_end - window_start + 1:
                    min_sub_sequence = S[window_start:window_end + 1]
                break

    return min_sub_sequence


# print(minWindow("abcdebdde", "bde"))
print(minWindow("hpsrhgogezyfrwfrejytjkzvgpjnqil", "sgy"))
