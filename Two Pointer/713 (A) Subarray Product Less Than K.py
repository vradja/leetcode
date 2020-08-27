from collections import deque


class Solution:

    # Here list the triplets that are less than target
    def numSubarrayProductLessThanK(self, nums, target: int):
        if target <= 1:  # we cannot have 0 in list.
            return 0
        count, product, window_start, triplets = 0, 1, 0, list()
        for window_end, window_end_value in enumerate(nums):
            product *= window_end_value
            while product >= target and window_start < len(nums):
                product /= nums[window_start]
                window_start += 1

            # make it deque and convert to list to make it a different object. Else its mutable and substitutes the temp_list variable
            temp_list = deque()

            # easy part to find the combinations from end to start, at each new number.
            # Cannot use slicing, because slicing does not give numbers in reverse with below logic
            for index in range(window_end, window_start - 1, -1):
                num = nums[index]
                temp_list.append(num)
                triplets.append(list(temp_list))
            count += window_end - window_start + 1  # gives all possible combinations.
        print("Count is " + str(count))
        return triplets


sol = Solution()
print(sol.numSubarrayProductLessThanK([8, 2, 6, 5], 50))
