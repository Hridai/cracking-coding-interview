"""
Problem:
Write code to remove duplicates from an unsorted linked list. How would you
solve this problem if a temporary buffer is not allowed?
"""

"""
Questions:


Algorithm:
I will use a hash map / dict. I, in this solution, will not solve without a
temporary buffer.

I will save, to a dict, every piece of data. Each time I find that the data
exists in that hash map, I will delete the current node from my linked list.


"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'utils'))
from linked_list import SinglyLinkedList


def remove_dups(list_in):
    d = {}
    ll = SinglyLinkedList.from_list(list_in)

    current = ll.head
    if current is None:
        return []
    d[current.data] = 1
    while current.next:
        if current.next.data in d:
            current.next = current.next.next
        else:
            d[current.next.data] = 1
            current = current.next
    return ll.to_list()


def test_func(list_in, expected_res):
    res = remove_dups(list_in)
    if res != expected_res:
        raise ValueError(f"{list_in} returned {res} but expected {expected_res}")


if __name__ == "__main__":
    test_func(["a", "b", "c", "b"], ["a", "b", "c"])
    test_func([], [])
    test_func(["a"], ["a"])
    test_func([1, 1, 1], [1])
    test_func([1, 2, 1, 2, 1], [1, 2])
    print("All tests passed.")
