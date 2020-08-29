def isHappy(num):
    def find_square_sum(num):
        sum = 0
        while num > 0:
            num, digit = divmod(num, 10)
            sum += digit ** 2
        return sum

    # find_square_sum = lambda n: sum(int(i) ** 2 for i in str(n))

    slow = fast = num
    while True:  # there is a cycle for sure in magic numbers problem
        slow = find_square_sum(slow)  # move one step
        fast = find_square_sum(find_square_sum(fast))  # move two steps
        if slow == fast:  # found the cycle
            return True if slow == 1 else False


def isHappy_2(num):  # using set
    s = set()
    while True:
        if num in s:
            return True if num == 1 else False
        else:
            s.add(num)
        num = sum(int(d) ** 2 for d in str(num))


def main():
    print(isHappy(23))
    print(isHappy(12))


main()
