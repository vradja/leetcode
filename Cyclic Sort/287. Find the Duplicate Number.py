def find_duplicate_1(nums):
    for i, num in enumerate(nums):
        while num != i + 1:  # while not in position
            if num == nums[num - 1]:
                return num
            nums[num - 1], nums[i] = num, nums[num - 1]
            num = nums[i]


def find_duplicate_2(nums):
    nums = [0] + nums
    for i, num in enumerate(nums):
        while num != i:  # while not in position
            if num == nums[num]:
                return num
            else:
                nums[num], nums[i] = num, nums[num]
                num = nums[i]


# IMPORTANT: There is a linked List slow and fast pointer solution to this, figure it out.
# If no edits to array are allowed. Use linked list

def find_duplicate(nums):  # Check LC 142
    slow = fast = head = nums[0]
    while fast < len(nums) and nums[fast] < len(
            nums):  # no reason to check for slow pointer, since its anyways slow and wont reach NULL before fast.
        slow, fast = nums[slow], nums[nums[fast]]
        if slow == fast:  # keep the intercept as it is already cycle length step ahead of head
            while head != slow:
                head, slow = nums[head], nums[slow]
            return head
    return None


def main():
    print(find_duplicate([1, 4, 3, 2, 4]))  # Cannot have number equal to or greater than len(nums)
    # print(find_duplicate([1, 4, 4, 3, 2]))
    # print(find_duplicate([2, 1, 3, 3, 5, 4]))
    # print(find_duplicate([2, 4, 1, 4, 4]))


main()
