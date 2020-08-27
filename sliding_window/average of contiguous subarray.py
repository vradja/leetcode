import functools
import itertools

# Given an array, find the average of all contiguous subarrays of size ‘K’ in it.


def find_averages_of_subarrays_1(K, arr):
    result = list()
    window_sum, window_start = 0.0, 0

    for windowEnd in range(len(arr)):
        window_sum += arr[windowEnd]
        window_start = windowEnd - K + 1

        if window_start >= 0:
            result.append(window_sum / K)  # find the average in first occurance of K Sum
            window_sum -= arr[window_start]  # Subtract the first element in window right after Sum calculation.

    return result


def find_averages_of_subarrays(K, arr):
    sums = [0] + list(itertools.accumulate(arr))
    # return list(map(lambda x: x/K, list(map(operator.sub, sums[K:], sums[:-K]))))
    return list(map(lambda start, end: (end - start) / K, sums[:-K], sums[K:]))


def find_averages_of_subarrays_3(K, arr):
    window_sum = functools.reduce(lambda x, y: x + y, arr[:K])
    result = [window_sum / K]

    for index, value in enumerate(arr[K:]):
        window_sum += value - arr[index]
        result.append(window_sum / K)

    return result


def find_averages_of_subarrays_4(K, arr):
    # Since the window is of fixed size K
    window_sum = sum(arr[:K])
    result = [window_sum / K]

    for window_start, value in enumerate(arr[K:]):
        window_sum += value - arr[window_start]
        result.append(window_sum / K)
    return result


def main():
    result = find_averages_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
    print("Averages of subarrays of size K: " + str(result))

    result = find_averages_of_subarrays(4, [1, 12, -5, -6, 50, 3])
    print("Averages of subarrays of size K: " + str(result))


main()
