"""
Problem:
You have two numbers represented by a linked list, where each node contains a
single digit. The digits are stored in reverse order, such that the 1's digit
is at the head of the list. Write a function that adds the two numbers and
returns the sum as a linked list. (You are not allowed to "cheat" and just
convert the linked list to an integer.)

FOLLOW UP: Suppose the digits are stored in forward order. Repeat the above
problem.
"""

"""
Questions:
- Are the digits guaranteed to be 0-9? Yes.
- Can the lists be different lengths? Yes.
- Can the result have more digits than either input (final carry)? Yes — e.g.
  999 + 1 = 1000.
- Should the output follow the same reversed convention as the input? Yes.

Algorithm (reverse order):
Walk both lists simultaneously, adding digits with carry propagation — the same
way you'd do addition by hand. Since digits are already in reverse order (1's
digit at head), we can process head-to-tail directly.

    7 -> 1 -> 6   (617)
  + 5 -> 9 -> 2   (295)
  ─────────────
    2 -> 1 -> 9   (912, stored reversed)

  Step 1: 7+5=12   → emit 2, carry=1
  Step 2: 1+9+1=11 → emit 1, carry=1
  Step 3: 6+2+1=9  → emit 9, carry=0

If one list is exhausted, treat missing digits as 0.
If carry remains after both lists are done, emit it as a final node.

Time:  O(max(n, m))
Space: O(max(n, m)) for the result list
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'utils'))
from linked_list import SinglyLinkedList


def sum_lists(node1, node2):
    result = SinglyLinkedList()
    carry = 0
    a, b = node1, node2

    while a or b or carry:
        digit_a = a.data if a else 0
        digit_b = b.data if b else 0

        total = digit_a + digit_b + carry
        carry = total // 10
        result.append(total % 10)

        if a: a = a.next
        if b: b = b.next

    return result


def test_func(l1, l2, expected):
    ll1 = SinglyLinkedList.from_list(l1)
    ll2 = SinglyLinkedList.from_list(l2)
    res = sum_lists(ll1.head, ll2.head).to_list()
    if res != expected:
        raise ValueError(f"Got {res}, expected {expected}")


if __name__ == "__main__":
    test_func([7, 1, 6], [5, 9, 2], [2, 1, 9])       # 617 + 295 = 912
    test_func([9, 9, 9], [1],       [0, 0, 0, 1])     # 999 + 1 = 1000 (final carry)
    test_func([1],       [9, 9, 9], [0, 0, 0, 1])     # different lengths, swapped
    test_func([0],       [0],       [0])               # zero + zero
    test_func([1],       [2],       [3])               # single digits
    print("All tests passed.")
