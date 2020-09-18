def merge(intervals_a, intervals_b):
    result = []
    for interval_a in intervals_a:
        for interval_b in intervals_b:
            start = max(interval_a[0], interval_b[0])
            end = min(interval_a[1], interval_b[1])
            if start <= end:  # if overlap exist
                result.append([start, end])

            if interval_a[1] < interval_b[1]: # if you predict no intersection, move to next entry in A
                break

    return result

# seems to be faster but I couldnt find the reason why.
def intervalIntersection(self, A, B):
    idx_a, idx_b = 0, 0
    size_a, size_b = len(A), len(B)

    intersection = []

    # Scan each possible interval pair
    while idx_a < size_a and idx_b < size_b:

        # Get start-time as well as end-time
        start_a, end_a = A[idx_a]
        start_b, end_b = B[idx_b]

        # Compute common start time and end time for current interval pair
        common_start = max(start_a, start_b)
        common_end = min(end_a, end_b)

        if common_start <= common_end:
            # Find one common overlapped interval
            intersection.append([common_start, common_end])

        if end_a <= end_b:
            # Try next interval of A
            idx_a += 1

        else:
            # Try next interval of B
            idx_b += 1

    return intersection


def main():
    print("Intervals Intersection: " + str(merge([[1, 3], [5, 6], [7, 9]], [[2, 3], [5, 7]])))
    print("Intervals Intersection: " + str(merge([[1, 3], [5, 7], [9, 12]], [[5, 10]])))


main()
