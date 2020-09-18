from heapq import *


class Meeting:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __lt__(self, other):
        # min heap based on meeting.end
        return self.end < other.end


# Best solution so far
def minMeetingRooms(self, intervals):
    min_heap = list()

    for interval in sorted(intervals, key=lambda x: x[0]):
        if min_heap and min_heap[0] <= interval[0]:  # only one room will replace another room.
            # use if for max overlapping. Use while for current overlapping
            heappop(min_heap)
            # Replace an already allocated room. Hence len(min_heap) will contain the min no of rooms needed, given the intervals.

        heappush(min_heap,interval[1])
        # store the ending time in heap to find the earliest closing time of meeting
        # This also allocates a new room everytime.

    return len(min_heap)


def min_meeting_rooms(meetings):
    # sort the meetings by start time
    meetings.sort(key=lambda x: x.start)

    minRooms = 0
    minHeap = []
    for meeting in meetings:
        # remove all the meetings that have ended
        while len(minHeap) > 0 and meeting.start >= minHeap[0].end:
            heappop(minHeap)
        # add the current meeting into min_heap
        heappush(minHeap, meeting)
        # all active meetings are in the min_heap, so we need rooms for all of them.
        minRooms = max(minRooms, len(minHeap))
    return minRooms


import heapq


def minMeetingRooms(intervals):
    intervals.sort(key=lambda x: x[0])
    heap = []  # stores the end time of intervals
    for i in intervals:
        if heap and i[0] >= heap[0]:
            # means two intervals can use the same room
            heapq.heapreplace(heap, i[1])
        else:
            # a new room is allocated
            heapq.heappush(heap, i[1])
    return len(heap)


def main():
    # print(minMeetingRooms([[0,30],[5,10],[15,20]]))
    print(minMeetingRooms([[4, 5], [2, 3], [2, 4], [3, 5]]))

    # print("Minimum meeting rooms required: " + str(min_meeting_rooms(
    #     [Meeting(4, 5), Meeting(2, 3), Meeting(2, 4), Meeting(3, 5)])))
    # print("Minimum meeting rooms required: " +
    #       str(min_meeting_rooms([Meeting(1, 4), Meeting(2, 5), Meeting(7, 9)])))
    # print("Minimum meeting rooms required: " +
    #       str(min_meeting_rooms([Meeting(6, 7), Meeting(2, 4), Meeting(8, 12)])))
    # print("Minimum meeting rooms required: " +
    #       str(min_meeting_rooms([Meeting(1, 4), Meeting(2, 3), Meeting(3, 6)])))
    # print("Minimum meeting rooms required: " + str(min_meeting_rooms(
    #     [Meeting(4, 5), Meeting(2, 3), Meeting(2, 4), Meeting(3, 5)])))


main()
