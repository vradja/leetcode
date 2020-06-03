from collections import Counter


def find_word_concatenation(string, words):
    if string == "" or len(words) == 0:
        return []

    result_indices, window_start = [], 0
    word_length = len(words[0])
    words_length = len(words)
    words_counter = Counter(words)
    window_length = words_length * word_length

    for window_end in range(window_length, len(string) + 1):
        window_words = [string[i:i + word_length] for i in range(window_start, window_end, word_length)]
        window_counter = Counter(window_words)
        if window_counter == words_counter:
            result_indices.append(window_start)

        window_start += 1

    return result_indices


def find_word_concatenation_2(string, words):
    result_indices, window_start = [], 0

    if string == "" or len(words) == 0:
        return result_indices

    word_length = len(words[0])
    words_length = len(words)
    window_length = words_length * word_length

    # moving window of fixed size
    for window_end in range(window_length, len(string)+1):  # we put -1 here, to make it inclusive
        matched = 0
        window_counter = Counter(words)

        # looping window
        for i in range(window_start, window_end, word_length): # we put +1 here to make it inclusive
            word = string[i:i + word_length]
            if word in window_counter:
                window_counter[word] -= 1
                if window_counter[word] == 0:
                    matched += 1
                elif window_counter[word] < 0:
                    break
                if matched == len(window_counter):
                    result_indices.append(window_start)
            else:
                break

        window_start += 1

    return result_indices


def main():
    # print(find_word_concatenation("catfoxcat", ["cat", "fox"]))
    # print(find_word_concatenation("catcatfoxfox", ["cat", "fox"]))
    # print(find_word_concatenation("barfoothefoobarman", ["foo","bar"]))
    print(find_word_concatenation("wordgoodgoodgoodbestword", ["word", "good", "best", "good"]))

    # print(find_word_concatenation("wordgoodgoodgoodbestword", ["word", "good", "best", "good"]))
    # print(find_word_concatenation("lingmindraboofooowingdingbarrwingmonkeypoundcake", ["fooo","barr","wing","ding","wing"]))


main()
