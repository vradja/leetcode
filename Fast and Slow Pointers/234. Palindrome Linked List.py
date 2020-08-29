class Node:
    def __init__(self, value, next=None):
        self.val = value
        self.next = next


def is_palindromic_linked_list(head):
    if not head:  # this condition has to be checked.
        return True

    slow = fast = head
    stack = [head.val]
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
        stack.append(slow.val)

    if fast is None:  # this means, there are even numbers in the list. Pop the last element in the stack
        stack.pop()

    while stack:
        if stack.pop() != slow.val:
            return False
        slow = slow.next
    return True


# Okayish solution
def is_palindromic_linked_list_2(head):
    lst = []
    while head:
        lst.append(head.val)
        head = head.next
    return lst == lst[::-1]


def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(2)

    print("Is palindrome: " + str(is_palindromic_linked_list(head)))

    head.next.next.next.next.next = Node(2)
    print("Is palindrome: " + str(is_palindromic_linked_list(head)))


main()
