# Time exceeded. Not so god approach to use slicing
def maxSlidingWindow_1(nums, k):
    max_list, window_start = [], 0
    for window_end in range(k, len(nums) + 1):
        max_list.append(max(nums[window_start:window_end]))
        window_start += 1
    return max_list

    # Good solution so far.


def maxSlidingWindow_2(nums, k):
    window_start, max_list = 0, list()
    max_list.append(max(nums[:k]))

    for window_end in range(k, len(nums)):
        if nums[window_start] == max_list[-1]:
            max_list.append(max(nums[window_start + 1:window_end + 1]))
        else:
            max_list.append(max(max_list[-1], nums[window_end]))

        window_start += 1

    return max_list


# Deque solution

from collections import deque


def remove_out_of_window_indices(deq, window_start):
    if window_start == deq[
        0]:  # No need to check for if deq, since dew will always have one element in window after the first pass
        deq.popleft()


def remove_smaller_value_indices(deq, nums, window_end_value):
    while deq and window_end_value > nums[deq[
        -1]]:  # need to check for while deq, since deq[-1] is possible in case all elements in window are less than current number.
        deq.pop()


def maxSlidingWindow_3(nums, k):
    # fixed length sliding window. store the initial k elements in deque sliding window.
    result, deq, window_start = list(), deque(), 0

    # store initial K values in a sliding window. In this case deque sliding window.
    for window_end, window_end_value in enumerate(nums[:k]):
        remove_smaller_value_indices(deq, nums, window_end_value)
        deq.append(window_end)
    result.append(nums[deq[0]])  # deq[0] always contains the largest number in the current window

    # iterate over the remaining values
    for index, window_end_value in enumerate(nums[k:]):
        window_end = index + k
        remove_out_of_window_indices(deq, window_start)
        remove_smaller_value_indices(deq, nums, window_end_value)
        deq.append(window_end)
        result.append(nums[deq[0]])
        window_start += 1

    return result

# Dynamic Programming
def maxSlidingWindow(nums, k):
    from_left = [0] * len(nums)
    from_right = [0] * len(nums)
    # Populate from right and from left
    for left_index, left_index_value in enumerate(nums):
        right_index = (len(nums) - 1) - left_index
        right_index_value = nums[right_index]

        # start of the block
        if left_index % k == 0:
            from_left[left_index] = left_index_value
        else:
            from_left[left_index] = max(from_left[left_index - 1], left_index_value)

        # end of the block OR last index in the array
        if right_index % k == (k - 1) or right_index == len(nums) - 1:
            from_right[right_index] = right_index_value
        else:
            from_right[right_index] = max(from_right[right_index + 1], right_index_value)

    result, window_start = list(), 0

    for window_end in range(k - 1, len(nums)):
        result.append(max(from_left[window_end], from_right[window_start]))
        window_start += 1

    return result


# print(maxSlidingWindow([1, -1], 1))
# print(maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
print(maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7, 1, 3, -1, 4], 4))
# print(maxSlidingWindow([7,2,4], 2))
