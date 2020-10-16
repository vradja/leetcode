from __future__ import print_function


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()


def reverse_1(head):  # grokking solution
    previous, current, next = None, head, None
    while current is not None:
        next = current.next  # temporarily store the next node
        current.next = previous  # reverse the current node
        previous = current  # before we move to the next node, point previous to the current node
        current = next  # move on the next node
    return previous


def reverse_2_1(head):
    prev = None
    while head:
        current = head
        head = head.next
        current.next = prev
        prev = current

    return prev


def reverse(head):  # Iterative solution
    prev = None
    while head:
        current, head = head, head.next  # move "head" forward
        current.next, prev = prev, current  # reverse "current" pointer and move "previous" forward

    return prev # return the prev since, prev = current


# Function to reverse the linked list
def reverse_3(head):
    if not (head and head.next):
        return head

    new_head = reverse(head.next)  # post-order traversal. Keep moving to the end.
    head.next.next, head.next = head, None  # reversal between head and head.next. Always make head.next = None, to make the front / old head to point to None. This will avoid infinite loop.
    return new_head


def reverse_4(head, prev=None):  # Not elegant but works. Using Previous
    if not (head and head.next):
        head.next = prev  # This is needed to reverse the last element.
        return head

    new_head = reverse(head.next, head)
    head.next = prev

    return new_head


def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(8)
    head.next.next.next.next = Node(10)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = reverse(head)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()


main()
