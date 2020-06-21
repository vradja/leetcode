# two pointer method

def pair_with_targetsum(arr, target_sum):
    # important to note here, that sorted takes a index, val and using lambda can be used to sort it at index 1.
    # Similar example can be found here: https://stackoverflow.com/questions/14218933/sorted-function-in-python
    arr = sorted(enumerate(arr), key=lambda x: x[1])
    start_index, end_index = 0, len(arr) - 1

    while start_index < end_index:
        current_sum = arr[start_index][1] + arr[end_index][1]

        if current_sum == target_sum:
            return [arr[start_index][0], arr[end_index][0]]
        elif current_sum < target_sum:
            start_index += 1
        else:
            end_index -= 1

    return [-1, -1]


# Using Hash

def pair_with_targetsum_3(arr, target_sum):
    d = dict()
    for index, value in enumerate(arr):
        complement = target_sum - arr[index]
        if complement in d:
            return [d[complement], index]
        else:
            d[value] = index

    return [-1, -1]


# print(pair_with_targetsum([1, 2, 3, 4, 6], 6))
# print(pair_with_targetsum([2, 5, 9, 11], 11))
# print(pair_with_targetsum([3, 2, 4], 6))
print(pair_with_targetsum([3, 3], 6))
