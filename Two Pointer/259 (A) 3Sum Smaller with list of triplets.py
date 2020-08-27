class Solution:
    def threeSumSmaller(self, nums, target: int):
        nums.sort()
        triplets = list()
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
                    for third_value in nums[l + 1: r + 1]:
                        triplets.append((item, nums[l], third_value))
                    l += 1
                else:
                    r -= 1
        return triplets


sol = Solution()
print(sol.threeSumSmaller([-1, 4, 2, 1, 3], 5))
# print(sol.threeSumSmaller([-1,1,-1,-1], -1))
