# This just gets the count

def remove_duplicates_1(arr):
    prev, count = None, len(arr)
    for index, value in enumerate(arr):
        if prev is not None and arr[prev] == value:
            count -= 1
        else:
            prev = index

    return count


# Better approach for count.
def remove_duplicates_2(arr):
    prev, count = 0, len(arr)
    for index in range(1, len(arr)):
        if arr[prev] == arr[index]:
            count -= 1
        else:
            prev = index

    return count


def remove_duplicates(nums) -> int:
    # lookup slice assignment
    nums[:] = sorted(set(nums)) # this will replace list in place
    # https://stackoverflow.com/questions/10623302/how-assignment-works-with-python-list-slice/10623352#10623352
    return len(nums)


# Here print the non duplicate elememnts only
def remove_duplicates_4(arr):
    prev = 0
    for index in range(1, len(arr)):
        if arr[prev] != arr[index]:  # if not duplicate
            prev += 1
            arr[prev] = arr[index]

    return prev + 1


# print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
# print(remove_duplicates([2, 2, 2, 11]))
print(remove_duplicates([1, 1, 2]))
