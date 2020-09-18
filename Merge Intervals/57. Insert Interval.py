def insert_1(intervals, newInterval):
    for index, interval in enumerate(intervals):
        if newInterval[0] <= interval[0]:
            intervals.insert(index, newInterval)
            newInterval = None
            break

    if not intervals or newInterval:
        intervals.append(newInterval)

    merged = list()
    for interval in intervals:
        if merged and interval[0] <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], interval[1])
        else:  # if merged is None or if both intervals are disjoint
            merged.append(interval)
    return merged


# faster solution due to Lambda
def insert_2(intervals, newInterval):
    merged = list()
    for interval in sorted(intervals + [newInterval], key=lambda x: x[0]):
        if merged and interval[0] <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], interval[1])
        else:  # if merged is None or if both intervals are disjoint
            merged.append(interval)
    return merged


def merge(merged, interval):
    if merged and interval[0] <= merged[-1][1]:
        merged[-1][1] = max(merged[-1][1], interval[1])
    else:  # if merged is None or if both intervals are disjoint
        merged.append(interval)


# Very complicated solution but worth a try
def insert_3(intervals, newInterval):
    merged = list()
    for interval in intervals:
        if newInterval and newInterval[0] < interval[0]:
            merge(merged, newInterval)
            newInterval = None
        merge(merged, interval)

    if newInterval:  # in case of [1,3], [2,5] => 2 gets missed out but needs to be merged. This will get missed during iteration, so have a flag.
        merge(merged, newInterval)

    return merged


def insert(intervals, new_interval):
    merged = []
    i, start, end = 0, 0, 1

    # skip (and add to output) all intervals that come before the 'new_interval'
    while i < len(intervals) and intervals[i][end] < new_interval[start]:
        merged.append(intervals[i])
        i += 1

    # merge all intervals that overlap with 'new_interval'
    while i < len(intervals) and intervals[i][start] <= new_interval[end]:
        new_interval[start] = min(intervals[i][start], new_interval[start])
        new_interval[end] = max(intervals[i][end], new_interval[end])
        i += 1

    # insert the new_interval
    merged.append(new_interval)

    # add all the remaining intervals to the output
    while i < len(intervals):
        merged.append(intervals[i])
        i += 1
    return merged


def main():
    print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 6])))
    # print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 10])))
    # print("Intervals after inserting the new interval: " + str(insert([[2, 3], [5, 7]], [1, 4])))
    # print("Intervals after inserting the new interval: " + str(insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8])))


main()
