def generate_valid_parentheses(nums):
    parentheses = [("", 0, 0)]
    balanced = False

    while not balanced:
        prev_level = parentheses.copy()
        parentheses.clear()
        balanced = True  # if balance becomes false, we need one more level for balancing
        for parenthesis, opened, closed in prev_level:
            if opened < nums:  # open parenthesis to the count of num
                parentheses.append((parenthesis + "(", opened + 1, closed))
                balanced = False

            if opened != closed:  # close till its balanced
                parentheses.append((parenthesis + ")", opened, closed + 1))

    return list(map(lambda x: x[0], parentheses))


def main():
    # print("All combinations of balanced parentheses are: " +
    #       str(generate_valid_parentheses(2)))
    print("All combinations of balanced parentheses are: " +
          str(generate_valid_parentheses(3)))


main()
