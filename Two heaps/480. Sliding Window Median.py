from heapq import *


class SlidingWindowMedian:
    def __init__(self):
        self.small = []
        self.large = []

    def rebalance_heaps(self):
        if len(self.large) < len(self.small):
            heappush(self.large, -heappop(self.small))
        elif len(self.large) - len(self.small) > 1:  # self.large can only be 1 more than small for median.
            heappush(self.small, -heappop(self.large))
        else:  # positive case where both large and small are equal or large is one more than small.
            pass  # this case you dont have to do anything

    def insert_num(self, num):
        if len(self.small) == len(self.large):
            heappush(self.large, -heappushpop(self.small, -num))
        else:
            heappush(self.small, -heappushpop(self.large, num))

    def remove_num(self, num):
        if num < self.large[0]:
            self.remove_from_heap(self.small, -num)
        else:
            self.remove_from_heap(self.large, num)

        self.rebalance_heaps()  # EXTREMELY IMPORTANT STEP

    def remove_from_heap(self, heap, num):
        ind = heap.index(num)  # find the element
        # move the element to the end and delete it
        heap[ind] = heap[-1]
        del heap[-1]
        heapify(heap)  # O(N) if heapify is used. Better to use this

        # PROTECTED METHOD: use only you want O(log N)
        # we can use heapify to readjust the elements but that would be O(N),
        # instead, we will adjust only one element which will O(logN)
        # if ind < len(heap):
        #     heapq._siftup(heap, ind)
        #     heapq._siftdown(heap, 0, ind)

    def find_median(self):
        if len(self.small) == len(self.large):
            return float(self.large[0] - self.small[0]) / 2.0
        else:
            return float(self.large[0])

    def find_sliding_window_median_1(self, nums, k):  # typical sliding solution. better one below
        result = []

        # list(map(lambda x: self.insert_num(x), nums[:k]))  # same as below
        [self.insert_num(x) for x in nums[:k]]
        result.append(self.find_median())

        for window_start, value in enumerate(nums[k:]):
            window_end = window_start + k
            self.remove_num(nums[window_end - k])
            self.insert_num(nums[window_end])
            result.append(self.find_median())

        return result

    def find_sliding_window_median(self, nums, k):  # better and sleek solution
        result = []

        for window_end, value in enumerate(nums):  # no need for slicing, we are taking care of this using if.
            self.insert_num(nums[window_end])
            # DO THIS STEP FIRST TO REMOVE, BEFORE FINDING THE MEDIAN
            if not window_end < k:  # same as window_end >= k
                self.remove_num(nums[window_end - k])
            if not window_end < k - 1:  # same as window_end >= k
                result.append(self.find_median())

        return result


def main():
    slidingWindowMedian = SlidingWindowMedian()
    result = slidingWindowMedian.find_sliding_window_median(
        [1, 2, -1, 3, 5], 2)
    print("Sliding window medians are: " + str(result))

    slidingWindowMedian = SlidingWindowMedian()
    result = slidingWindowMedian.find_sliding_window_median(
        [1, 2, -1, 3, 5], 3)
    print("Sliding window medians are: " + str(result))


main()
