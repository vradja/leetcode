import bisect


class Solution:
    def find_median(self, window, k):
        if k % 2 == 0:
            return (window[k // 2] + window[(k // 2) - 1]) / 2
        else:
            return window[k // 2]

    def medianSlidingWindow(self, nums, k):
        window_start = 0
        window = sorted(nums[window_start:k])
        medians = [self.find_median(window, k)]

        for window_end_char in nums[k:]:
            window.remove(nums[window_start])  # remove window_start
            window_start += 1
            bisect.insort(window, window_end_char)  # add window_end
            medians.append(self.find_median(window, k))

        return medians

sol = Solution()
print(sol.medianSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
