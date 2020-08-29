from __future__ import print_function


class Node:
    def __init__(self, value, next=None):
        self.val = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(str(temp.val) + " ", end='')
            temp = temp.next
        print()


def reorderList(head):
    """
    :type head: ListNode
    :rtype: None Do not return anything, modify head in-place instead.
    """
    if not head:
        return head

    slow = fast = head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next

    # do this to reverse the rest of the list
    middle = slow
    slow = slow.next
    middle.next = None

    stack = list()
    while slow:
        temp = slow
        slow = slow.next
        temp.next = None
        stack.append(temp)

    # now insert in between.
    while stack:
        temp = head.next
        head.next = stack.pop()
        head.next.next = temp
        head = head.next.next


def reverse(head):
    prev = None
    while head is not None:
        next = head.next
        head.next = prev
        prev = head
        head = next
    return prev


def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(8)
    head.next.next.next.next = Node(10)
    head.next.next.next.next.next = Node(12)
    reorderList(head)
    head.print_list()


main()
