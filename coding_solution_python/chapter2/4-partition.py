"""
Problem:
Write code to partition a linked list around a value x, such that all nodes
less than x come before all nodes greater than or equal to x. If x is
contained within the list, the values of x only need to be after the elements
less than x (see below). The partition element x can appear anywhere in the
"right partition"; it does not need to appear between the left and right
partitions.
"""

"""
Questions:
- Should relative order within each partition be preserved? Not required by the
  problem, but a good interview answer does preserve it — it demonstrates a cleaner
  algorithm and is easier to reason about.
- Modify in-place or return a new structure? We reuse existing nodes (O(1) extra
  space beyond the result pointers) and return a new list head.
- Can the list be empty? Yes — return an empty list.
- Can x be absent from the list? Yes — the partition property still holds.
- Can x be smaller than all elements, or larger than all? Yes — one partition
  will be empty.

Algorithm:
Two-pointer two-list technique. Maintain head and tail pointers for a "left"
partition (values < x) and a "right" partition (values >= x). Walk the original
list once, routing each node to the appropriate partition tail in O(1). After the
walk, join left_tail -> right_head.

    Input:  [3, 5, 8, 5, 10, 2, 1], x=5

    left:   3 -> 2 -> 1
    right:  5 -> 8 -> 5 -> 10

    joined: 3 -> 2 -> 1 -> 5 -> 8 -> 5 -> 10

Nodes are reused (detached and re-linked), so no extra node allocations.

Time:  O(n)
Space: O(1) extra  (only four pointer variables; result reuses original nodes)
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'utils'))
from linked_list import SinglyLinkedList


def partition(ll, x):
    left_head = left_tail = None
    right_head = right_tail = None

    current = ll.head
    while current:
        next_node = current.next
        current.next = None  # detach before re-linking

        if current.data < x:
            if left_head is None:
                left_head = left_tail = current
            else:
                left_tail.next = current
                left_tail = current
        else:
            if right_head is None:
                right_head = right_tail = current
            else:
                right_tail.next = current
                right_tail = current

        current = next_node

    # Join: left_tail -> right_head (handle empty partitions)
    if left_head is None:
        result_head = right_head
    elif right_head is None:
        result_head = left_head
    else:
        left_tail.next = right_head
        result_head = left_head

    result = SinglyLinkedList()
    result.head = result_head
    return result


def assert_valid_partition(values, x):
    """Property-based assertion: verifies partition correctness, not exact order."""
    ll = SinglyLinkedList.from_list(values)
    result = partition(ll, x).to_list()

    # All elements < x must precede all elements >= x
    seen_right = False
    for v in result:
        if v >= x:
            seen_right = True
        if seen_right and v < x:
            raise ValueError(f"Partition violated for x={x}: {result}")

    # Same multiset of elements
    if sorted(result) != sorted(values):
        raise ValueError(f"Elements changed for x={x}: got {result}, had {values}")


if __name__ == "__main__":
    assert_valid_partition([3, 5, 8, 5, 10, 2, 1], 5)   # standard case, x present
    assert_valid_partition([3, 5, 8, 5, 10, 2, 1], 7)   # x not in list
    assert_valid_partition([1, 2, 3], 10)                 # all elements < x
    assert_valid_partition([5, 6, 7], 3)                  # all elements >= x
    assert_valid_partition([5], 5)                        # single element, equals x
    assert_valid_partition([3], 5)                        # single element, less than x
    assert_valid_partition([], 5)                         # empty list
    assert_valid_partition([1, 1, 1], 1)                  # all equal to x

    # Verify order is preserved within each partition
    ll = SinglyLinkedList.from_list([3, 5, 8, 5, 10, 2, 1])
    result = partition(ll, 5).to_list()
    assert result == [3, 2, 1, 5, 8, 5, 10], f"Order not preserved: {result}"

    print("All tests passed.")
