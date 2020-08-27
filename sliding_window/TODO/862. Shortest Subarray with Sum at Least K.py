# Need to redo this problem


class Solution:
    def shortestSubarray(self, A, K: int) -> int:
        window_sum, window_start = 0.0, 0
        min_sum_count = float("inf")

        for window_end, value in enumerate(A):
            window_sum += value

            while window_sum >= K:
                min_sum_count = min(min_sum_count, window_end - window_start + 1)
                window_sum -= A[window_start]
                window_start += 1

        return min_sum_count if min_sum_count != float("inf") else -1


def main():
    sol = Solution()
    print("Smallest subarray length: " + str(sol.shortestSubarray([84, -37, 32, 40, 95], 167)))
    # Solution should be 3, but we get 5. Learn the deque solution.


main()
