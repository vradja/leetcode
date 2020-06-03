import collections


class Solution:
    def longestOnes(self, arr, K: int) -> int:
        window_start, longest_sub_string, max_repeating_ones_count, replaceable_count = 0, 0, 0, 0
        freq_counter = collections.Counter()

        for window_end, value in enumerate(arr):
            freq_counter[value] += 1

            # max_repeating_ones_count = max(max_repeating_ones_count, freq_dict[1])
            # or
            # max_repeating_ones_count = freq_dict[1]
            # replaceable_count = (window_end - window_start + 1) - max_repeating_ones_count

            if freq_counter[0] > K:
                freq_counter[arr[window_start]] -= 1
                window_start += 1

            longest_sub_string = (window_end - window_start + 1)

        return longest_sub_string

    def longestOnes_1(self,arr, K):
        window_start, longest_substring, max_ones_count, replaceable_count = 0, 0, 0, 0
        # No need for dict, since it is specified only 1's are needed in maximum sequence. Just keep track of 1's

        for window_end, value in enumerate(arr):
            max_ones_count += arr[window_end]
            replaceable_count = (window_end - window_start + 1) - max_ones_count

            if replaceable_count > K:
                max_ones_count -= arr[window_start]
                window_start += 1

            longest_substring = window_end - window_start + 1
        return longest_substring

def main():
    sol = Solution()
    print(sol.longestOnes([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2))
    print(sol.longestOnes([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3))

main()
