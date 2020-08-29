class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def has_cycle(head):
    slow = fast = head
    while fast is not None and fast.next is not None: # no reason to check for slow pointer, since its anyways slow and wont reach NULL before fast.
        slow, fast = slow.next, fast.next.next
        if slow == fast:
            return True
        else:
            return False

def main():
    head = Node(1)
    head.next = Node(2)
    print("LinkedList has cycle: " + str(has_cycle(head)))

    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    print("LinkedList has cycle: " + str(has_cycle(head)))

    head.next.next.next.next.next.next = head.next.next
    print("LinkedList has cycle: " + str(has_cycle(head)))

    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList has cycle: " + str(has_cycle(head)))


main()
