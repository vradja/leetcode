class Solution:
    def sortedSquares_1(self, arr: List[int]) -> List[int]:
        squares = list()
        left, right = 0, len(arr) - 1
        while left <= right:  # needs to reach the last element in the middle.
            left_value_square, right_value_square = arr[left] ** 2, arr[right] ** 2
            if left_value_square < right_value_square:
                squares.insert(0, right_value_square)
                right -= 1
            else:
                squares.insert(0, left_value_square)
                left += 1

        return squares

        # faster solution, since sorted() is timsort and O(n). Making this the fastest solution.

    def sortedSquares(self, arr):
        return sorted([x ** 2 for x in arr])
