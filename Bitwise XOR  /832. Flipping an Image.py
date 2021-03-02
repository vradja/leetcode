# Naive method
def flip_an_invert_image_1(matrix):
    matrix_length = len(matrix)
    for row in matrix:
        for i in range((matrix_length + 1) // 2):
            row[i], row[matrix_length - 1 - i] = row[matrix_length - 1 - i] ^ 1, row[i] ^ 1

    return matrix


# Better method in pythonic way. Here row[len(matrix) -1 -i] is same as row[-i -1]
def flip_an_invert_image_2(matrix):
    for row in matrix:
        for i in range((len(matrix) + 1) // 2):
            row[i], row[-i - 1] = row[-i - 1] ^ 1, row[i] ^ 1

    return matrix


# using lambda and map
def flip_an_invert_image_3(matrix):
    for i, row in enumerate(matrix):
        matrix[i] = (list(map(lambda x: x ^ 1, row[::-1])))
    return matrix


# using list_comprehension, easy version
def flip_an_invert_image_4(matrix):
    for i, row in enumerate(matrix):
        matrix[i] = [num ^ 1 for num in row[::-1]]
    return matrix


# using list_comprehension, single line version
def flip_an_invert_image_5(matrix):
    return [[num ^ 1 for num in row[::-1]] for row in matrix]


# using list_comprehension, single line version, USING REVERSED
def flip_an_invert_image(matrix):
    return [[num ^ 1 for num in reversed(row)] for row in matrix]


def main():
    print(flip_an_invert_image([[1, 0, 1], [1, 1, 1], [0, 1, 1]]))
    print(flip_an_invert_image([[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]))


main()
