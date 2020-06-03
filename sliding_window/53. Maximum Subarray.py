import itertools


# Approach 1

def max_sub_array_of_size_k_1(K, arr):
    window_sum = sum(arr[:K])
    max_sum = window_sum

    for window_start, value in enumerate(arr[K:]):
        window_sum += value - arr[window_start]
        max_sum = max(max_sum, window_sum)

    return max_sum


# Approach 2:

def max_sub_array_of_size_k(K, arr):
    cumulative_sums = [0] + list(itertools.accumulate(arr))
    return max(map(lambda begin, end: end - begin, cumulative_sums[:-K], cumulative_sums[K:]))


def main():
    print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2])))
    print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5])))


main()
