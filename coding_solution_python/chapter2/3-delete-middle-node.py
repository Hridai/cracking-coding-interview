"""
Problem:
Implement an algorithm to delete a node in the middle (i.e., any node but
the first and last node, not necessarily the exact middle) of a singly linked
list, given only access to that node.
"""

"""
Questions:
- Are we guaranteed the node is not the tail? Yes — the problem states any node
  but the last. The copy trick requires node.next to exist.
- Do we return anything? No — modify the list in-place.
- Can the list have fewer than 3 nodes? No — a valid middle node requires at least
  one node before and after it.

Algorithm:
Copy trick — because we have no reference to the previous node, we can't do the
standard prev.next = node.next. Instead, overwrite the current node's data with
the next node's data, then skip over the next node.

    Before: ... -> [node: 3] -> [next: 4] -> [5] -> ...
    Step 1: node.data = next.data    → [node: 4] -> [next: 4] -> [5] -> ...
    Step 2: node.next = next.next    → [node: 4] -> [5] -> ...

The node effectively "becomes" its successor, and the successor is discarded.

Time:  O(1)
Space: O(1)
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'utils'))
from linked_list import SinglyLinkedList


def delete_middle_node(node):
    node.data = node.next.data
    node.next = node.next.next


def test_func(list_in, target_value, expected_result):
    ll = SinglyLinkedList.from_list(list_in)
    node = ll.find(target_value)
    delete_middle_node(node)
    if ll.to_list() != expected_result:
        raise ValueError(f"Got {ll.to_list()}, expected {expected_result}")


if __name__ == "__main__":
    test_func([1, 2, 3, 4, 5], 3, [1, 2, 4, 5])      # exact middle
    test_func([1, 2, 3, 4, 5], 2, [1, 3, 4, 5])      # second node
    test_func([1, 2, 3, 4, 5], 4, [1, 2, 3, 5])      # second to last
    test_func([1, 2, 3, 4, 5, 6], 2, [1, 3, 4, 5, 6]) # even-length list
    print("All tests passed.")
