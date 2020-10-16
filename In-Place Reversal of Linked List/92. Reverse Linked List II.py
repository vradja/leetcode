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


def reverse(head, index, maximum):
    if not (head and head.next) or index == maximum:
        return head, head.next  # return both head and hext.next since, we need the end.next to be stitched. It is okay if this is None

    new_head, new_head_next = reverse(head.next, index + 1, maximum)  # post-order traversal. Keep moving to the end.
    head.next.next, head.next = head, None  # reversal between head and head.next. Always make head.next = None, to make the front / old head to point to None. This will avoid infinite loop.
    return new_head, new_head_next


# Recursive Solution
def reverse_sub_list(head, p, q):
    # STEP 1: Move the sublist_head pointer to first element to be reversed.
    prev, sublist_head = None, head
    for i in range(2, p + 1):
        prev = sublist_head
        sublist_head = sublist_head.next
    end = sublist_head

    # STEP 2: # return the previous similar to LL reversal, since sublist_prev == sublist_curr
    if prev:  # this is when p > 1 and STEP 2 is executed.
        # STEP 3: Assign end.next to end of reversed List.
        prev.next, end.next = reverse(sublist_head, 0, q - p)
    else:
        # STEP 3: Assign end.next to end of reversed List.
        head, end.next = reverse(sublist_head, 0, q - p)  # This is when p is 1

    return head


def reverse_sub_list_2(head, p, q):  # Elegnant and Best Solution
    # NO need to do p==q since our solution is already generic and will handle this situation.

    # STEP 1: Move the sublist_head pointer to first element to be reversed.
    prev, sublist_head = None, head
    for i in range(2, p + 1):
        prev = sublist_head
        sublist_head = sublist_head.next
    end = sublist_head

    # STEP 2: Do usual LL reversal.
    sublist_prev = None
    for i in range(p, q + 1):  # no need to check for if sublist_head, since p & q are less than length of list.
        sublist_curr, sublist_head = sublist_head, sublist_head.next
        sublist_curr.next, sublist_prev = sublist_prev, sublist_curr

    # STEP 3: # return the previous similar to LL reversal, since sublist_prev == sublist_curr
    if prev:  # this is when p > 1 and STEP 2 is executed.
        prev.next = sublist_prev
    else:
        head = sublist_prev  # This is when p is 1

    # STEP 4: Assign end.next to end of reversed List.
    end.next = sublist_head  # this can be None if last element OR it can be element after reversal of sublist.

    return head


def reverse_sub_list_3(head, p, q):
    prev, curr = None, head  # curr = head because p will be 1 or more. So initialize to head for p = 1, to start with.
    for i in range(2, p + 1):  # since curr is already in head, we already moved one step. start at 2 now.
        prev = curr
        curr = curr.next

    # curr is the new "head" here
    sub_prev, sub_curr, sub_end = None, curr, curr
    for i in range(p, q + 1):  # Usual Linked List Reversal
        sub_curr, curr = curr, curr.next
        sub_curr.next, sub_prev = sub_prev, sub_curr

    if prev:
        prev.next = sub_curr
    else:
        head = sub_curr

    sub_end.next = curr

    return head


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = reverse_sub_list(head, 2, 4)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()


main()
