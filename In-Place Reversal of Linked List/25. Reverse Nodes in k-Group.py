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


def reverse_iterative(head, k, remain):  # Iterative solution
    prev = None
    for i in range(k):
        if not head:
            if remain:
                prev, head = None, current
                while head:
                    current, head = head, head.next
                    current.next, prev = prev, current
            break
        current, head = head, head.next  # move "head" forward
        current.next, prev = prev, current  # reverse "current" pointer and move "previous" forward

    return prev, head  # return the prev since, prev = current


def reverse_recursive(head, k, count):  # Recursive Solution
    if not head or not head.next or count == k:
        return head, head.next, count
    # post-order traversal. Keep moving to the end until K
    new_head, next_sublist_head, sublist_count = reverse_recursive(head.next, k, count + 1)
    head.next.next, head.next = head, None  # reversal between head and head.next. Always make head.next = None, to make the front / old head to point to None. This will avoid infinite loop.
    return new_head, next_sublist_head, sublist_count


# Recursive Recursive Solution
def reverse_every_k_elements_1(head, k, remain=False):
    new_head, next_sublist_head, count = reverse_recursive(head, k, 1)
    if remain and count < k:
        new_head, next_sublist_head, count = reverse_recursive(new_head, k, 1)
    if next_sublist_head:
        head.next = reverse_every_k_elements(next_sublist_head, k, remain)
    return new_head


# Recursive Iterative  Solution : BEST SOLUTION
def reverse_every_k_elements_2(head, k, remain=False):
    new_head, next_sublist_head = reverse_iterative(head, k, remain)
    if next_sublist_head:
        head.next = reverse_every_k_elements(next_sublist_head, k, remain)
    return new_head


# Iterative solution
def reverse_every_k_elements_3(head, k, remain=False):  # Remain == True is if size(sublist) is less than k
    # STEP 1: Find new_head for first sublist reversal. Need sublist_end for stiching to next reversed sublist.
    new_head, sublist_end = None, None

    # STEP 2: Outer loop to reverse every occurance of sublist with size >= k
    while head:

        # STEP 3: Regular LL reversal.
        prev, first = None, head  # store the "first" of sublist to be re-assigned to sublist_end for next iteration.
        for i in range(k):
            if not head:
                if remain:  # this is generic solution to re-reverse it back to original.
                    prev, head = None, curr  # curr will always be populated, since while head passed, which means there is atleast one element in sublist
                    while head:
                        curr, head = head, head.next
                        curr.next, prev = prev, curr
                break
            curr, head = head, head.next
            curr.next, prev = prev, curr

        # STEP 4: stitch the reversed list to sublist_end or assign new head.
        if not new_head:  # will set the first reversed sublist to head, happens only once
            new_head = prev
        else:
            sublist_end.next = prev

        # STEP 5: re-assign the first to sublist_end to be stitched with next reversed list.
        sublist_end = first

    return new_head


# Iterative Iterative Solution
def reverse_every_k_elements_4(head, k, remain=False):
    # STEP 1: Find new_head for first sublist reversal. Need sublist_end for stiching to next reversed sublist.
    new_head, sublist_end = None, None

    # STEP 2: Outer loop to reverse every occurance of sublist with size >= k
    while head:

        first = head

        # STEP 3: Regular LL reversal.
        prev, head = reverse_iterative(head, k, remain)

        # STEP 4: stitch the reversed list to sublist_end or assign new head.
        if not new_head:  # will set the first reversed sublist to head, happens only once
            new_head = prev
        else:
            sublist_end.next = prev

        # STEP 5: re-assign the first to sublist_end to be stitched with next reversed list.
        sublist_end = first

    return new_head


# Iterative Recursive Solution
def reverse_every_k_elements(head, k, remain=False):
    # STEP 1: Find new_head for first sublist reversal. Need sublist_end for stiching to next reversed sublist.
    new_head, sublist_end = None, None

    # STEP 2: Outer loop to reverse every occurance of sublist with size >= k
    while head:

        first = head

        # STEP 3: Regular LL reversal.
        prev, head, count = reverse_recursive(head, k, 1)
        if remain and count < k:
            prev, head, count = reverse_recursive(prev, k, 1)

        # STEP 4: stitch the reversed list to sublist_end or assign new head.
        if not new_head:  # will set the first reversed sublist to head, happens only once
            new_head = prev
        else:
            sublist_end.next = prev

        # STEP 5: re-assign the first to sublist_end to be stitched with next reversed list.
        sublist_end = first

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
    result = reverse_every_k_elements(head, 3, False)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()


main()
