"""
Problem:
Implement an algorithm to find the kth to last element of a singly linked list.
k is 1-indexed: k=1 returns the last element, k=2 returns the second-to-last, etc.
"""

"""
Questions:
- Is k 1-indexed (k=1 = last) or 0-indexed? Assume 1-indexed per CTCI convention.
- What should we return if k > length of the list? Return None.
- Can the list be empty? Assume no, but handle k out-of-bounds gracefully.
- Should we return the node or the value? Return the value (clarify with interviewer).

Algorithm:
Two-pointer (runner) technique — no need to know the list length in advance.

Advance a 'fast' pointer k steps ahead of 'slow'. Then walk both forward in sync
until 'fast' falls off the end (becomes None). At that point, 'slow' is exactly
k nodes from the tail.

        [1] -> [2] -> [3] -> [4] -> [5] -> None     k=2
fast starts at head, advances 2 steps: fast = node(3)
then walk both until fast is None:
    fast=4, slow=2
    fast=5, slow=3
    fast=None, slow=4  <-- return slow.data = 4

If fast reaches None during the initial advance, k > length: return None.

Time:  O(n) — single pass after the k-step advance
Space: O(1) extra — two pointers only (the linked list itself is not rebuilt)
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'utils'))
from linked_list import SinglyLinkedList


def kth_to_last(head, k):
    fast = head
    slow = head

    for _ in range(k):
        if fast is None:
            return None  # k exceeds list length
        fast = fast.next

    while fast:
        fast = fast.next
        slow = slow.next

    return slow.data


def test_func(list_in, k, expected):
    ll = SinglyLinkedList.from_list(list_in)
    res = kth_to_last(ll.head, k)
    if res != expected:
        raise ValueError(f"{res} != {expected}")


if __name__ == "__main__":
    test_func([1, 2, 3, 4, 5], 1, 5)          # last element
    test_func([1, 2, 3, 4, 5], 2, 4)          # second to last
    test_func([1, 2, 3, 4, 5], 5, 1)          # first element (k == len)
    test_func([1, 2, 3, 4, 5, 6, 7, 8], 4, 5) # middle
    test_func([7], 1, 7)                       # single element
    test_func([1, 2, 3], 10, None)             # k > length → None
    print("All tests passed.")
