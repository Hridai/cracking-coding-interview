"""
Problem:
Implement a function to check if a linked list is a palindrome.
"""

"""
Questions:


Algorithm:


"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'utils'))
from linked_list import SinglyLinkedList, SNode


def palindrome_checker(head_node):

    def reverse_ll(node):
        reverse_ll_head = None  # prepend all node values to this, to form reversed ll
        while node:
            new_node = SNode(node.data)
            new_node.next = reverse_ll_head
            reverse_ll_head = new_node  # save the result outside loop, to then append onto the next loop, this is a prepend operation
            node = node.next
        new_ll = SinglyLinkedList()
        new_ll.head = reverse_ll_head
        return new_ll

    def ll_equality_check(ll_head, reversed_ll_head):
        ll_node = ll_head
        ll_reverse_node = reversed_ll_head
        while ll_node and ll_reverse_node:
            if ll_node.data != ll_reverse_node.data:
                return False
            ll_node = ll_node.next
            ll_reverse_node = ll_reverse_node.next
        return True

    ll_reversed = reverse_ll(head_node)
    return ll_equality_check(head_node, ll_reversed.head)


def test_func(l_in, expected_result):
    ll = SinglyLinkedList.from_list(l_in)
    res = palindrome_checker(ll.head)
    if res != expected_result:
        raise ValueError(f"Result {res} does not match expected result {expected_result}")


if __name__ == "__main__":
    test_func([1,2,3,2,1], True)
    test_func([1,2,3,2,2], False)
