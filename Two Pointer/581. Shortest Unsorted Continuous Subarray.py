class Solution(object):

    # Best solution, check for follow_up questions.
    # there is an another solution in grokking, check that out.
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start, end, prev_low, prev_high = None, None, None, None

        for i, next_high in enumerate(nums):
            if prev_low is None or prev_low <= next_high:
                prev_low = next_high
            else:
                end = i

        for i, next_low in reversed(list(enumerate(nums))):
            if prev_high is None or next_low <= prev_high:
                prev_high = next_low
            else:
                start = i

        if start is not None and end is not None:
            return end - start + 1
        else:
            return 0


sol = Solution()

# print(sol.findUnsortedSubarray([1, 5, 3, 2, 4, 6, 7, 8]))
# print(sol.findUnsortedSubarray([1,2,3,4]))
# print(sol.findUnsortedSubarray([1, 2, 3, 3, 3]))
print(sol.findUnsortedSubarray([2, 6, 4, 8, 5, 10, 9, 15]))
