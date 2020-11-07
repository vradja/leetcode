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


def reverse_iterative(head, k, reverse):
    prev = None
    for _ in range(k):
        if not head:
            break
        current, head = head, head.next

        if reverse:
            current.next, prev = prev, current
        else:
            prev = current

    return prev, head


def reverse_alternate_k_elements(head, k, reverse=True):
    prev, next_sublist_head = reverse_iterative(head, k, reverse)

    if next_sublist_head:
        if reverse:
            head.next = reverse_alternate_k_elements(next_sublist_head, k, not reverse)
        else:
            prev.next = reverse_alternate_k_elements(next_sublist_head, k, not reverse)

    return prev if reverse else head  # return here, because there is a possibility of next_sublist_head being false.


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)
    head.next.next.next.next.next.next.next = Node(8)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = reverse_alternate_k_elements(head, 2)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()


main()
