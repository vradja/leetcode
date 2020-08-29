def circular_array_loop_exists_1(nums):
    indexToNext = {index: (index + value) % len(nums) for index, value in enumerate(nums)}
    increment = {key: value for key, value in indexToNext.items() if key != value}

    while len(increment) > 0:

        if any(index == nextIndex for index, nextIndex in increment.items()):
            return True

        increment = {index: indexToNext[nextIndex]
                     for index, nextIndex in increment.items()
                     if nums[index] * nums[nextIndex] > 0 and nextIndex in increment}

    return False


def circular_array_loop_exists(arr):
    for i, num in enumerate(arr):
        is_forward = num >= 0  # if we are moving forward or not
        slow, fast = i, i

        # if slow or fast becomes '-1' this means we can't find cycle for this number
        while True:
            # move one step for slow pointer
            slow = find_next_index(arr, is_forward, slow)
            # move one step for fast pointer
            fast = find_next_index(arr, is_forward, fast)
            if fast != -1:
                # move another step for fast pointer
                fast = find_next_index(arr, is_forward, fast)

            if slow == -1 or fast == -1 or slow == fast:
                break

        if slow != -1 and slow == fast:
            return True

    return False


def find_next_index(arr, is_forward, current_index):
    direction = arr[current_index] >= 0

    if is_forward != direction:
        return -1  # change in direction, return -1

    next_index = (current_index + arr[current_index]) % len(arr)

    # one element cycle, return -1
    if next_index == current_index:
        next_index = -1

    return next_index


def main():
    print(circular_array_loop_exists([1, 2, -1, 2, 2]))
    print(circular_array_loop_exists([2, 2, -1, 2]))
    print(circular_array_loop_exists([2, 1, -1, -2]))


main()
