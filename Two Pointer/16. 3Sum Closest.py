import bisect


class Solution:
    def threeSumClosest_1(self, nums, target: int) -> int:
        nums.sort()
        closestSum = None
        howClose = float("inf")
        for i, item in enumerate(nums[:-2]):
            l = i + 1
            r = len(nums) - 1
            while (l < r):
                value = item + nums[l] + nums[r]

                if value == target:
                    return value

                difference = abs(target - value)

                if difference < howClose:
                    closestSum = value
                    howClose = difference

                if value < target:
                    l += 1
                else:
                    r -= 1

        return closestSum

    # HashMap and Recursions do not work for closest and less than problems. Makes it complicated. Stick with Iterative
    # approach

    # Binary search between two pointer solution for Triplet.
    # Fastest solution
    def threeSumClosest_2(self, nums, target: int) -> int:
        nums.sort()
        seen, closest_sum, how_close, third_val = dict(), float('inf'), float('inf'), None
        for first, first_val in enumerate(nums[:-2]):
            for second in range(first + 1, len(nums) - 1):
                second_val = nums[second]
                required_third = target - first_val - second_val
                if required_third not in seen:
                    seen[required_third] = True
                else:
                    continue

                mid = bisect.bisect(nums, required_third, lo=second + 1)

                # https://stackoverflow.com/questions/12141150/from-list-of-integers-get-number-closest-to-a-given-value/12141511#12141511

                if mid == second + 1:
                    third_val = nums[mid]
                elif mid == len(nums):
                    third_val = nums[mid - 1]
                else:
                    before = nums[mid - 1]
                    after = nums[mid]

                    # on LEFT: required_third will become negative if after, or it stays positive
                    if after - required_third < required_third - before:
                        third_val = after
                    else:
                        third_val = before

                value = first_val + second_val + third_val

                if value == target:
                    return target

                difference = abs(target - value)

                if difference < how_close:
                    closest_sum = value
                    how_close = difference

        return closest_sum

    def threeSumClosest(self, nums, target: int) -> int:
        # nums.sort() # No need to sort here
        seen, closest_sum, how_close, third_val = dict(), float('inf'), float('inf'), None
        for first, first_val in enumerate(nums[:-2]):
            for second in range(first + 1, len(nums) - 1):
                second_val = nums[second]
                required_third = target - first_val - second_val
                if required_third not in seen:
                    seen[required_third] = True

                    # Interesting solution using Lambda and min
                    third_val = min(nums[second + 1:], key=lambda x: abs(x - required_third))

                    value = first_val + second_val + third_val

                    if value == target:
                        return target

                    difference = abs(target - value)

                    if difference < how_close:
                        closest_sum = value
                        how_close = difference

        return closest_sum


sol = Solution()
# print(sol.threeSumClosest([-1,2,1,-4], 1))
print(sol.threeSumClosest([1, 1, -1, -1, 3], -1))
# print(sol.threeSumClosest([-1,2,1,-4], 1))
# print(sol.threeSumClosest([1,2,4,8,16,32,64,128], 82))
