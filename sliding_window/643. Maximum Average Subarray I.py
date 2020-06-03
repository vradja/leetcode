# Approach 1
import functools
import itertools
import operator

import numpy as np

# Approach 1

def find_max_average_1(arr, K):
    # P = [0]
    #
    # # Do cumulative addition at each index
    # for x in arr:
    #     P.append(P[-1] + x)
    # P[-1] gives the last index's value in the list

    # OR

    P = [0] + list(itertools.accumulate(arr))


    # ma = 0
    # for i in range(len(arr) - K + 1):
    #     ma = max(P[i + K] - P[i], ma)

    # This step substracts sumulative index with the another cumulative index, giving us Sum value of just we want.
    # ma = max(P[i+K] - P[i] for i in range(len(arr) - K + 1))

    # OR

    ma = max(map(operator.sub, P[K:], P[:-K]))

    return ma / float(K)

# Approach 2

def find_max_average_2(arr, K):
    window_sum, window_start = 0.0, -K
    max_sum = -float("inf")

    for window_end, value in enumerate(arr):
        window_sum += value
        window_start += 1

        if window_start >= 0:
            max_sum = max(window_sum, max_sum)
            window_sum -= arr[window_start]

    return max_sum / K

# Approach 3

def find_max_average_3(nums, k):
    sums = [0] + list(itertools.accumulate(nums))
    return max(map(operator.sub, sums[k:], sums)) / k

# Approach 4

def find_max_average_4(nums, k):
    sums = np.cumsum([0] + nums)
    # return int(max(sums[k:] - sums[:-k])) / k
    return max(map(operator.sub, sums[k:], sums[:-k])) / k

# Approach 5

def find_max_average(nums, k):
    # m = a = sum(nums[:k])
    # OR
    window_sum = functools.reduce(lambda x, y: x + y, nums[:k])
    max_sum = window_sum
    # for i in range( k, len(nums) ):
    #     a += ( nums[i] - nums[i-k] )
    #     if a > m: m = a
    for index, value in enumerate(nums[k:]):
        window_sum += value - nums[index]
        if window_sum > max_sum: max_sum = window_sum
    return max_sum/k

def main():
    print(find_max_average([1, 3, 2, 6, -1, 4, 1, 8, 2],5))
    print(find_max_average([1, 12, -5, -6, 50, 3],4))

main()
