import operator
from functools import reduce


def find_single_numbers(nums):
    # calculate bitwise leads to difference between 2 unique numbers
    bitmask = reduce(operator.xor, nums)
    # Here bitmask follows the rule that a^b = bitmask => a^bitmask = b => b^bitmask = a

    # hint: split them into 2 groups based on their rightmost 1 or 2 unique number's difference.
    # hint: x & -x = right_most_1.
    # here -x = ~x + 1
    right_most_1 = bitmask & -bitmask

    # x & -x is similar to the below implementation:
    rightmost_set_bit = 1  # we arent using this anywhere below. This is for example only.
    while (rightmost_set_bit & bitmask) == 0:
        rightmost_set_bit = rightmost_set_bit << 1  # here we keep moving left, till we find the 1. As we know 2 numbers
        # are unique, this bitmask cannot be 0, and it should defer by atleast 1 bit and we end up finding the rightmost

    first_unique_number = 0
    # Now iterate all the numbers that has rightmost 1
    for num in nums:
        if num & right_most_1:  # if both numbers have similar rightmost 1
            first_unique_number ^= num

    # here first_unique_number ^ bitmask is the category that is num & right_most_1 are different.
    # Since we already found bitmask which is difference between 2 unique number.
    # first_unique_number ^ bitmask => bitmask contains unique numbers a ^ b. Now if we found a then xoring a with a^b,
    # leads to b. That is (a^b) ^ a = b.
    return [first_unique_number, first_unique_number ^ bitmask]


def main():
    print('Single numbers are:' +
          str(find_single_numbers([1, 4, 2, 1, 3, 5, 6, 2, 3, 5])))
    print('Single numbers are:' + str(find_single_numbers([2, 1, 3, 2])))


main()
