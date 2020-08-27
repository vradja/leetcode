class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        current, left, right = 0, 0, len(nums) - 1

        while current <= right:
            current_char = nums[current]
            if current_char == 0:
                nums[left], nums[current] = nums[current], nums[left]
                left += 1
                current += 1  # need to increment, because we know 1 is swapped with 0.
            elif current_char == 2:
                nums[right], nums[current] = nums[current], nums[right]
                right -= 1
                # do not increment i, we do not know what is swapped from high
            else:
                current += 1
        return nums


sol = Solution()
print(sol.sortColors([2, 0, 1]))
