'''

Try solving these problems too:
252 Meeting Rooms
253 Meeting Rooms II
435 Non-overlapping Intervals
56 (A) Given a set of intervals, find out if any two intervals overlap.
'''



from __future__ import print_function


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end='')


def merge_1(intervals):
    merged, start, end = list(), None, None
    for interval in sorted(intervals, key=lambda x: x.start):  # important NOTE this
        if not start:
            start = interval.start
            end = interval.end

        # if start <= interval.start <= end: # You can remove start here, since the list is already sorted and the start will always be less than interval.start
        if interval.start <= end:
            end = max(end, interval.end)
        else:
            merged.append(Interval(start, end))
            start = interval.start
            end = interval.end

    merged.append(Interval(start, end))  # NOTE: we need to do this for adding last pair

    return merged


# Space efficient solution but can give it a try: Store evr
def merge(intervals):
    merged = list()
    for interval in sorted(intervals, key=lambda x: x.start):
        if merged and interval.start < merged[-1].end:
            merged[-1].end = max(merged[-1].end, interval.end)
        else:
            merged.append(interval)
    return merged


def main():
    print("Merged intervals: ", end='')
    for i in merge([Interval(1, 4), Interval(2, 5), Interval(7, 9)]):
        i.print_interval()
    print()

    print("Merged intervals: ", end='')
    for i in merge([Interval(6, 7), Interval(2, 4), Interval(5, 9)]):
        i.print_interval()
    print()

    print("Merged intervals: ", end='')
    for i in merge([Interval(1, 4), Interval(2, 6), Interval(3, 5)]):
        i.print_interval()
    print()


main()
