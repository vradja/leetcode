from itertools import accumulate


class Solution:
    def maxSatisfied_1(self, customers, grumpy, X) -> int:
        # find largest sum in window. here windowlength in X

        window_start, satisfied_customers = 0, 0,
        max_window_indices_range = (window_start, X - 1)
        max_grumpy_window_sum = grumpy_window_sum = sum(
            value for index, value in enumerate(customers[:X]) if grumpy[index])

        for index, window_end_char in enumerate(customers[X:]):
            window_end = index + X

            if grumpy[window_end]:
                grumpy_window_sum += window_end_char

            if grumpy[window_start]:
                grumpy_window_sum -= customers[window_start]

            window_start += 1

            if max_grumpy_window_sum < grumpy_window_sum:
                max_grumpy_window_sum = grumpy_window_sum
                max_window_indices_range = (window_start, window_end)

        for index in range(0, len(customers)):
            if not grumpy[index]:
                satisfied_customers += customers[index]
            elif max_window_indices_range[0] <= index <= max_window_indices_range[1]:
                satisfied_customers += customers[index]
            else:
                pass

        return satisfied_customers

    # Approach 2: Here add the already satisfied customer count and make them 0, then run sliding window.
    def maxSatisfied_2(self, customers, grumpy, X):
        satisfied_customers = 0
        for index, customers_count in enumerate(customers):
            if grumpy[index] == 0:
                satisfied_customers += customers_count
                customers[index] = 0

        # now sliding window the remaining customers when grumpy. Find the max customers when he is grumpy.
        max_window_sum, window_start = sum(customers[:X]), 0
        window_sum = max_window_sum

        for window_end_value in customers[X:]:
            window_sum += window_end_value - customers[window_start]
            window_start += 1
            if window_sum > max_window_sum:
                max_window_sum = window_sum

        satisfied_customers += max_window_sum

        return satisfied_customers

    # Approach 2 A. Merging 2 for loops into one.
    def maxSatisfied_2_a(self, customers, grumpy, X):
        window_start, satisfied_customers, max_window_sum, window_sum = 0, 0, 0, 0

        for window_end, customer_count in enumerate(customers):
            if grumpy[window_end] == 0:
                satisfied_customers += customer_count
                customers[window_end] = 0
            else:
                window_sum += customer_count

            if window_end >= X:  # fixed window_size reached
                window_sum -= customers[window_start]
                window_start += 1

            if window_sum > max_window_sum:
                max_window_sum = window_sum

        return satisfied_customers + max_window_sum

    # not so good approach, works nonetheless
    def maxSatisfied_3(self, customers, grumpy, X):
        window_start, satisfied_customers, max_window_sum, window_sum = 0, 0, 0, 0

        for window_end, (customer_count, is_grumpy) in enumerate(zip(customers, grumpy)):
            satisfied_customers += customer_count * (not is_grumpy)
            customers[window_end] = customers[window_end] * is_grumpy
            window_sum += customer_count * is_grumpy

            if window_end >= X:  # fixed window_size reached
                window_sum -= customers[window_start]
                window_start += 1

            if window_sum > max_window_sum:
                max_window_sum = window_sum

        return satisfied_customers + max_window_sum

    # prefix sum approach
    def maxSatisfied(self, customers, grumpy, X):
        satisfied_customers = sum(value for index, value in enumerate(customers) if not grumpy[index])
        dis_satisfied_customers = [value if grumpy[index] else 0 for index, value in enumerate(customers)]

        # prefix sum calculation
        prefix_sum = [0] + list(accumulate(dis_satisfied_customers))
        window_start, max_window_sum = 0, 0
        for index, value in enumerate(prefix_sum[X:]):
            window_end = index + X
            max_window_sum = max(max_window_sum, value - prefix_sum[window_start])
            window_start += 1

        return satisfied_customers + max_window_sum


sol = Solution()

# print(sol.maxSatisfied([2, 6, 6, 9], [0, 0, 1, 1], 1))
print(sol.maxSatisfied([1, 0, 1, 2, 1, 1, 7, 5], [0, 1, 0, 1, 0, 1, 0, 1], 3))
# print(sol.maxSatisfied([9, 10, 4, 5], [1, 0, 1, 1], 1))
