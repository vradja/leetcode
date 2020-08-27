from collections import Counter


class Solution:

    def remove_from_counter(self, freq_d, val):
        freq_d[val] -= 1
        if freq_d[val] == 0:
            freq_d.pop(val, None)

    def lengthOfLongestSubstringKDistinct_1(self, s: str, k: int) -> int:
        freq_counter, window_start, longest_substring = Counter(), 0, 0

        for window_end, value in enumerate(s):
            freq_counter[value] += 1

            while len(freq_counter) > k:
                self.remove_from_counter(freq_counter, s[window_start])
                window_start += 1

            longest_substring = max(longest_substring, window_end - window_start + 1)

        return longest_substring

    def lengthOfLongestSubstringKDistinct(self, s, k):
        index_dict = dict()
        window_start, longest_substring = 0, 0
        for window_end, value in enumerate(s):
            index_dict[value] = window_end
            if len(index_dict) > k:
                window_start = min(index_dict.values())
                # Here delete is required, since it is an update operation for future characters.
                index_dict.pop(s[window_start], None)
                window_start += 1
            longest_substring = max(window_end - window_start + 1, longest_substring)
        return longest_substring


def main():
    sol = Solution()
    print(sol.lengthOfLongestSubstringKDistinct("ecebaab", 2))


main()
