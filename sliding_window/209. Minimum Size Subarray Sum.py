def smallest_subarray_with_given_sum_1(s, arr):
    window_sum, window_start = 0.0, 0
    min_sum = float("inf")

    for window_end, value in enumerate(arr):
        window_sum += value
        while window_sum >= s:
            min_sum = min(min_sum, window_end - window_start + 1)
            window_sum -= arr[window_start]
            window_start += 1

    return min_sum if min_sum != float("inf") else 0


# prefix sum approach
from itertools import accumulate


def smallest_subarray_with_given_sum(s, arr):
    cumulative_sum = [0] + list(accumulate(arr))
    window_start, window_sum, smallest_subarray = 0, 0.0, float("inf")
    for window_end, value in enumerate(cumulative_sum):
        window_sum = value - cumulative_sum[window_start]
        while window_sum >= s:
            smallest_subarray = min(smallest_subarray, window_end - window_start)
            window_start += 1
            window_sum = value - cumulative_sum[window_start]
    return smallest_subarray if smallest_subarray != float("inf") else 0


def main():
    print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2])))
    print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8])))
    print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6])))


main()
