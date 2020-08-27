class Solution:

    # iterative method
    def threeSum(self, arr):
        triplets = set()
        duplicate = dict()
        arr.sort()  # better sort here than sorting each tuple in two_sum
        for index, value in enumerate(arr[:-2]):
            if value not in duplicate:
                self.two_sum(arr[index + 1:], -value, triplets)
            else:
                duplicate[value] = index
        return triplets

    def two_sum_1(self, arr, target, triplets):
        left, right = 0, len(arr) - 1
        while left < right:  # here equal to is not needed, since we want 2 distinct numbers.
            left_value, right_value = arr[left], arr[right]
            two_sum = left_value + right_value
            if target == two_sum:
                triplets.append((-target, left_value, right_value))  # move left and right since we found a match
                left += 1
                right -= 1
            elif two_sum < target:
                left += 1
            else:
                right -= 1

    def two_sum(self, arr, target, triplets):
        d = dict()
        for index, value in enumerate(arr):
            complement = target - value
            if complement in d:
                triplets.add((-target, complement, value))
            else:
                d[value] = index


sol = Solution()
print(sol.threeSum([-3, 0, 1, 2, -1, 1, -2]))
# print(search_triplets([-5, 2, -1, -2, 3]))
