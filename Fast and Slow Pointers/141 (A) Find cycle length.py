class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def find_cycle_length_1(head):
    slow = fast = head
    cycle_length = 0
    while fast is not None and fast.next is not None:  # no reason to check for slow pointer, since its anyways slow and wont reach NULL before fast.
        slow, fast = slow.next, fast.next.next
        if slow == fast:
            slow, cycle_length = slow.next, 1
            while slow != fast:
                slow = slow.next
                cycle_length += 1
            return cycle_length
    else:
        return cycle_length


# Better solution. Both pointers intersect at cycle length.
def find_cycle_length(head):
    slow = fast = head
    cycle_length = 0
    while fast is not None and fast.next is not None:  # no reason to check for slow pointer, since its anyways slow and wont reach NULL before fast.
        slow, fast = slow.next, fast.next.next
        cycle_length += 1
        if slow == fast:
            return cycle_length


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = head.next.next
    print("LinkedList cycle length: " + str(find_cycle_length(head)))

    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList cycle length: " + str(find_cycle_length(head)))


main()
