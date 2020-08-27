import bisect


class Solution:
    def threeSumSmaller_1(self, arr, target):
        count = 0
        arr.sort()
        for first, first_value in enumerate(arr[:-2]):
            for second in range(first + 1, len(arr) - 1):
                second_value = arr[second]
                required_third = target - first_value - second_value  # -1 needed here to get closest

                third_start = second + 1
                third = bisect.bisect_left(arr, required_third, lo=third_start)

                if third == third_start:
                    if arr[third] < required_third:
                        count += third - third_start + 1
                elif third == len(arr):
                    if arr[third - 1] < required_third:
                        count += (third - 1) - third_start + 1
                else:  # 2 cases
                    before = arr[third - 1]
                    after = arr[third]
                    # Find which is less than .
                    if after < required_third:
                        count += third - third_start + 1
                    elif before < required_third:
                        count += (third - 1) - third_start + 1
        return count

    def threeSumSmaller(self, nums, target: int):
        nums.sort()
        count = 0
        for i, item in enumerate(nums[:-2]):

            if not 3 * item < target:
                break

            l = i + 1
            r = len(nums) - 1
            new_target = target - item

            while l < r:
                if not 2 * nums[l] < new_target:
                    break

                value = nums[l] + nums[r]
                if value < new_target:
                    count += r - l  # Important step to count all possible combinations in terms of multiple index
                    l += 1
                else:
                    r -= 1
        return count


sol = Solution()
# print(sol.threeSumSmaller([-1, 4, 2, 1, 3], 5))
print(sol.threeSumSmaller([-1, 1, -1, -1], -1))
