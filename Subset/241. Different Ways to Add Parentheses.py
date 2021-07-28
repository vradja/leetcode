def diff_ways_to_evaluate_expression(input, memo=dict()):  # Can do faster. Check leetcode discuss
    if input.isdigit():
        return [eval(input)]

    if input in memo:
        return memo[input]

    result = []

    for index, char in enumerate(input):

        if char in "+-*":
            left = diff_ways_to_evaluate_expression(input[:index])
            right = diff_ways_to_evaluate_expression(input[index + 1:])
            result.extend((eval(str(x) + char + str(y)) for x in left for y in right))

    memo[input] = result

    return result


def main():
    print("Expression evaluations: " +
          str(diff_ways_to_evaluate_expression("1+2*3")))
    print("Expression evaluations: " +
          str(diff_ways_to_evaluate_expression("2*3-4-5")))


main()
