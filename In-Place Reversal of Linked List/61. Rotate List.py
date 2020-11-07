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


def rotate(head, k):
    if k == 0 or not head:  # here k == 0 is optional.
        return head

    prev, curr, count = None, head, 0
    while curr:
        prev, curr = curr, curr.next
        count += 1

    if k % count == 0: # this one step improved Time compexity.
        return head

    prev.next = head

    #  This "count - k % count" will give us head. Start counting from back, to move to front.
    # take count = 7 and k = 2, we will have to move last 2 to front, but to find what it is, we have to walk 5 times.
    for _ in range(count - k % count):
        prev, head = head, head.next

    prev.next = None

    return head


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = rotate(head, 3)
    print("Nodes of rotated LinkedList are: ", end='')
    result.print_list()


main()
