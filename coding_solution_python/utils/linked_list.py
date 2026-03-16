"""
Utility classes for singly and doubly linked lists.
Used by Chapter 2 (and beyond) solutions.

Import example:
    import sys, os
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'utils'))
    from linked_list import SinglyLinkedList, DoublyLinkedList
"""


# ---------------------------------------------------------------------------
# Singly Linked List
# ---------------------------------------------------------------------------

class SNode:
    """A node in a singly linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"SNode({self.data})"


class SinglyLinkedList:
    """
    Singly linked list with O(1) append and O(n) search/delete.

    Supports:
        append(data)        — add to tail
        prepend(data)       — add to head
        delete(data)        — remove first node with matching data
        find(data)          — return first node with matching data, or None
        to_list()           — return Python list of values (head → tail)
        __len__             — number of nodes
        __iter__            — iterate over node data values
        __repr__            — human-readable string
    """

    def __init__(self):
        self.head = None
        self._length = 0

    @classmethod
    def from_list(cls, items):
        """Build a SinglyLinkedList from a Python list."""
        ll = cls()
        for item in items:
            ll.append(item)
        return ll

    def append(self, data):
        """Add a new node to the tail. O(n)."""
        new_node = SNode(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self._length += 1

    def prepend(self, data):
        """Add a new node to the head. O(1)."""
        new_node = SNode(data)
        new_node.next = self.head
        self.head = new_node
        self._length += 1

    def delete(self, data):
        """Remove the first node whose data matches. O(n)."""
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            self._length -= 1
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                self._length -= 1
                return
            current = current.next

    def find(self, data):
        """Return the first node with matching data, or None. O(n)."""
        current = self.head
        while current:
            if current.data == data:
                return current
            current = current.next
        return None

    def to_list(self):
        """Return all values as a Python list. O(n)."""
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def __len__(self):
        return self._length

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

    def __repr__(self):
        return " -> ".join(str(v) for v in self) + " -> None"


# ---------------------------------------------------------------------------
# Doubly Linked List
# ---------------------------------------------------------------------------

class DNode:
    """A node in a doubly linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __repr__(self):
        return f"DNode({self.data})"


class DoublyLinkedList:
    """
    Doubly linked list with O(1) append/prepend and O(n) search/delete.

    Supports:
        append(data)        — add to tail
        prepend(data)       — add to head
        delete(data)        — remove first node with matching data
        find(data)          — return first node with matching data, or None
        to_list()           — return Python list of values (head → tail)
        __len__             — number of nodes
        __iter__            — iterate over node data values (head → tail)
        __repr__            — human-readable string
    """

    def __init__(self):
        self.head = None
        self.tail = None
        self._length = 0

    @classmethod
    def from_list(cls, items):
        """Build a DoublyLinkedList from a Python list."""
        dll = cls()
        for item in items:
            dll.append(item)
        return dll

    def append(self, data):
        """Add a new node to the tail. O(1)."""
        new_node = DNode(data)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self._length += 1

    def prepend(self, data):
        """Add a new node to the head. O(1)."""
        new_node = DNode(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self._length += 1

    def delete(self, data):
        """Remove the first node whose data matches. O(n)."""
        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                self._length -= 1
                return
            current = current.next

    def find(self, data):
        """Return the first node with matching data, or None. O(n)."""
        current = self.head
        while current:
            if current.data == data:
                return current
            current = current.next
        return None

    def to_list(self):
        """Return all values as a Python list. O(n)."""
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def __len__(self):
        return self._length

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

    def __repr__(self):
        return "None <-> " + " <-> ".join(str(v) for v in self) + " <-> None"


# ---------------------------------------------------------------------------
# Demo
# ---------------------------------------------------------------------------

if __name__ == "__main__":

    print("=== SinglyLinkedList ===")

    sll = SinglyLinkedList()
    sll.append(1)
    sll.append(2)
    sll.append(3)
    sll.prepend(0)
    print(f"After appending 1,2,3 and prepending 0: {sll}")
    print(f"Length: {len(sll)}")

    # from_list convenience constructor
    sll2 = SinglyLinkedList.from_list([10, 20, 30, 40])
    print(f"from_list([10,20,30,40]): {sll2}")

    # find
    node = sll2.find(20)
    print(f"find(20): {node}")
    print(f"find(99): {sll2.find(99)}")

    # delete head
    sll2.delete(10)
    print(f"After delete(10): {sll2}")

    # delete middle
    sll2.delete(30)
    print(f"After delete(30): {sll2}")

    # delete tail
    sll2.delete(40)
    print(f"After delete(40): {sll2}")

    # iterate
    sll3 = SinglyLinkedList.from_list(["a", "b", "c"])
    print(f"Iterating: {[v for v in sll3]}")

    # access head directly (useful in chapter 2 solutions)
    print(f"head node: {sll3.head}, head.next: {sll3.head.next}")

    print()
    print("=== DoublyLinkedList ===")

    dll = DoublyLinkedList()
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.prepend(0)
    print(f"After appending 1,2,3 and prepending 0: {dll}")
    print(f"Length: {len(dll)}")
    print(f"head: {dll.head}, tail: {dll.tail}")

    # from_list
    dll2 = DoublyLinkedList.from_list([10, 20, 30, 40])
    print(f"from_list([10,20,30,40]): {dll2}")

    # find
    node = dll2.find(30)
    print(f"find(30): {node}, prev={node.prev}, next={node.next}")

    # delete head
    dll2.delete(10)
    print(f"After delete(10): {dll2}, new head={dll2.head}")

    # delete tail
    dll2.delete(40)
    print(f"After delete(40): {dll2}, new tail={dll2.tail}")

    # delete middle
    dll2.delete(20)
    print(f"After delete(20): {dll2}")

    # backwards traversal via prev pointers
    dll3 = DoublyLinkedList.from_list([1, 2, 3, 4, 5])
    current = dll3.tail
    backwards = []
    while current:
        backwards.append(current.data)
        current = current.prev
    print(f"Backwards traversal: {backwards}")

    print()
    print("All demos complete.")
