import operator
from functools import reduce


# Solution 1: Basic solution using XOR

def find_single_number_1(arr):
    num = 0
    for i in arr:
        num ^= i
    return num


# Solution 2: Using Reduce Lambda and XOR
def find_single_number(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    return reduce(lambda x, y: x ^ y, nums)


# Solution 3: Using Only Reduce and XOR
def find_single_number_3(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    return reduce(operator.xor, nums)


def main():
    arr = [1, 4, 2, 1, 3, 2, 3]
    print(find_single_number(arr))


main()
