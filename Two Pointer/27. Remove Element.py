class Solution:
    def removeElement(self, nums, val):
        prev = 0
        for index in range(0, len(nums)):
            # start here at range 0, since we are looking for removing the number val. We are not looking for
            # duplicates in an array.
            if nums[index] != val:
                nums[prev] = nums[index]
                prev += 1
        return prev
        # return nums[:prev]


sol = Solution()
print(sol.removeElement([3, 2, 2, 3], 3))
