from heapq import *


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end


# LEETCODE TESTCASE FAILS. TEST AGAIN WITH DIFFERENT APPROACH LIKE BISECT

# EASILY THE BEST SOLUTION AVAILABLE.
def find_next_interval(intervals):
    min_heap_start_intervals = sorted(enumerate(intervals),
                                      key=lambda x: x[1])  # DO NOT USE HEAP AFTER SORTING. SINCE HEAP CANNOT
    # BE EASILY PUSHED WITH A DIFFERENT INDEX
    res = [-1] * len(intervals)
    minheap = []
    for interval in min_heap_start_intervals:
        right, (start, end) = interval

        if start == end:  # each interval itself is allowed to be considered to be its interval if start == end
            res[right] = right
        else:
            while minheap and minheap[0][0] <= start:
                _, left = heappop(minheap)
                res[left] = right
            heappush(minheap, [end, right])
    return res


def find_next_interval_2(intervals):
    # heaps for finding the maximum start and end
    maxStartHeap, maxEndHeap = [], []

    # result = [-1 for _ in range(len(intervals))] # We can use this or below statement.
    result = [-1] * len(intervals)
    for index in range(len(intervals)):
        heappush(maxStartHeap, (-intervals[index].start, index))
        heappush(maxEndHeap, (-intervals[index].end, index))

    # go through all the intervals to find each interval's next interval
    for _ in intervals:
        # let's find the next interval of the interval which has the highest 'end'
        topEnd, endIndex = heappop(maxEndHeap)
        if -maxStartHeap[0][0] >= -topEnd:
            topStart, startIndex = heappop(maxStartHeap)
            # find the the interval that has the closest 'start'
            while maxStartHeap and -maxStartHeap[0][0] >= -topEnd:
                topStart, startIndex = heappop(maxStartHeap)
            result[endIndex] = startIndex
            # put the interval back as it could be the next interval of other intervals
            heappush(maxStartHeap, (topStart, startIndex))

    return result


def main():
    # result = find_next_interval(
    #     [Interval(2, 3), Interval(3, 4), Interval(5, 6), Interval(7, 8)])
    # print("Next interval indices are: " + str(result))

    # result = find_next_interval(
    #     [Interval(3, 4), Interval(1, 5), Interval(4, 6)])
    # print("Next interval indices are: " + str(result))

    # result = find_next_interval(
    #     [Interval(3, 4), Interval(5, 6), Interval(4, 7)])
    # result = find_next_interval([[2, 4], [3, 6], [4, 7]])

    # result = find_next_interval([[15, 16], [1, 12], [16, 17], [2, 9], [13, 14], [3, 10]])
    # print("Next interval indices are: " + str(result))

    result = find_next_interval([[1, 1], [3, 4]])
    print("Next interval indices are: " + str(result))


main()
