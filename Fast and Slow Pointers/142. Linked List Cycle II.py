from __future__ import print_function


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end='')
            temp = temp.next
        print()


def find_cycle_length(head):
    slow = fast = head
    while fast is not None and fast.next is not None:  # no reason to check for slow pointer, since its anyways slow and wont reach NULL before fast.
        slow, fast = slow.next, fast.next.next
        if slow == fast:
            slow, cycle_length = slow.next, 1
            while slow != fast:
                slow = slow.next
                cycle_length += 1
            return cycle_length
    else:
        return 0


def cycle_start(head, cycle_length):
    if cycle_length == 0:
        return None

    slow = fast = head
    step = 0

    while step < cycle_length:
        fast = fast.next
        step += 1

    while slow != fast:
        slow, fast = slow.next, fast.next

    return slow


def find_cycle_start_1(head):
    cycle_length = find_cycle_length(head)
    return cycle_start(head, cycle_length) if cycle_length != 0 else None


# Better solution
def find_cycle_start(head):
    slow = fast = head
    while fast is not None and fast.next is not None:  # no reason to check for slow pointer, since its anyways slow and wont reach NULL before fast.
        slow, fast = slow.next, fast.next.next
        if slow == fast: # keep the intercept as it is already cycle length step ahead of head
            while head != slow:
                head, slow = head.next, slow.next
            return head

def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    head.next.next.next.next.next.next = head.next.next
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))

    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))

    head.next.next.next.next.next.next = head
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))


main()
