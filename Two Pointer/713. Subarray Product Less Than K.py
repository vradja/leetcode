class Solution:
    def numSubarrayProductLessThanK(self, nums, target: int) -> int:
        if target <= 1:  # we cannot have 0 in list.
            return 0
        count, product, window_start = 0, 1, 0
        for window_end, window_end_value in enumerate(nums):
            product *= window_end_value
            while product >= target and window_start < len(nums):
                product /= nums[window_start]
                window_start += 1
            count += window_end - window_start + 1  # gives all possible combinations.
        return count
