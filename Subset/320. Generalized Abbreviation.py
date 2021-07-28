# This could be a recursion. MUST TRY. # Exactly similar to Generate parantheses
def generate_generalized_abbreviation(word):
    abbrevations = [("", 0)]
    for char in word:
        previous_level = abbrevations.copy()
        abbrevations.clear()

        for string, count in previous_level:
            abbrevations.append([string, count + 1])
            abbrevations.append([(string + str(count) if count else string) + char, 0])

    return list(map(lambda x: x[0] + str(x[1]) if x[1] else x[0], abbrevations))


def main():
    print("Generalized abbreviation are: " +
          str(generate_generalized_abbreviation("BAT")))
    # print("Generalized abbreviation are: " +
    #       str(generate_generalized_abbreviation("code")))


main()
