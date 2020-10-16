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


def reverse_every_k_elements(head, k):
    # STEP 1: Find new_head for first sublist reversal
    new_head = None

    # STEP 2: Outer loop to reverse every occurance of size K sublist
    while head:

        # STEP 3: Regular LL reversal. here sublist_end is needed to reassign this reversed link to next sublists's prev
        prev, sublist_end = None, head
        for i in range(k):
            if not head:
                break
            curr, head = head, head.next
            curr.next, prev = prev, curr

        if not new_head:  # will set the first reversed sublist to head, happens only once
            new_head = prev
        else:
            sublist_end.next = prev

    return new_head


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
    result = reverse_every_k_elements(head, 3)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()


main()
