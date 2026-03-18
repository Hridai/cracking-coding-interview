"""
Utility class for a stack backed by a singly linked list.
Used by Chapter 3 (and beyond) solutions.

Import example:
    import sys, os
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'utils'))
    from stack import Stack
"""


# ---------------------------------------------------------------------------
# Stack node
# ---------------------------------------------------------------------------

class _StackNode:
    """Internal node used by Stack."""
    def __init__(self, data):
        self.data = data
        self.next = None  # points toward the bottom of the stack


# ---------------------------------------------------------------------------
# Stack
# ---------------------------------------------------------------------------

class Stack:
    """
    LIFO stack backed by a linked list. All core operations are O(1).

    Supports:
        push(data)      — add item to top
        pop()           — remove and return top item  (raises IndexError if empty)
        peek()          — return top item without removing (raises IndexError if empty)
        is_empty()      — True if stack has no items
        __len__         — number of items
        __iter__        — iterate top → bottom (non-destructive)
        __repr__        — human-readable string  (top → bottom)

    Intentionally minimal: Chapter 3 problems extend or wrap this class
    rather than getting a kitchen-sink implementation up front.
    """

    def __init__(self):
        self._top = None       # _StackNode or None
        self._size = 0

    @classmethod
    def from_list(cls, items):
        """
        Build a Stack from a Python list.
        The *last* element of the list becomes the top of the stack,
        matching the intuition of pushing items left-to-right.

            Stack.from_list([1, 2, 3])  →  top: 3, bottom: 1
        """
        s = cls()
        for item in items:
            s.push(item)
        return s

    # ------------------------------------------------------------------
    # Core operations
    # ------------------------------------------------------------------

    def push(self, data):
        """Add item to the top. O(1)."""
        node = _StackNode(data)
        node.next = self._top
        self._top = node
        self._size += 1

    def pop(self):
        """Remove and return the top item. O(1). Raises IndexError if empty."""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        data = self._top.data
        self._top = self._top.next
        self._size -= 1
        return data

    def peek(self):
        """Return the top item without removing it. O(1). Raises IndexError if empty."""
        if self.is_empty():
            raise IndexError("peek at empty stack")
        return self._top.data

    def is_empty(self):
        """Return True if the stack contains no items. O(1)."""
        return self._top is None

    # ------------------------------------------------------------------
    # Dunder helpers
    # ------------------------------------------------------------------

    def __len__(self):
        return self._size

    def __iter__(self):
        """Iterate over values from top to bottom (non-destructive)."""
        current = self._top
        while current:
            yield current.data
            current = current.next

    def __repr__(self):
        items = " -> ".join(str(v) for v in self)
        return f"Stack(top -> {items} -> bottom)"


# ---------------------------------------------------------------------------
# Demo / self-test
# ---------------------------------------------------------------------------

if __name__ == "__main__":

    print("=== Stack ===")

    s = Stack()
    assert s.is_empty()
    assert len(s) == 0

    s.push(1)
    s.push(2)
    s.push(3)
    print(f"After push 1,2,3: {s}")
    assert len(s) == 3
    assert s.peek() == 3

    top = s.pop()
    print(f"pop() -> {top}, stack now: {s}")
    assert top == 3
    assert s.peek() == 2
    assert len(s) == 2

    # from_list: last element should be on top
    s2 = Stack.from_list([10, 20, 30])
    print(f"from_list([10,20,30]): {s2}")
    assert s2.pop() == 30
    assert s2.pop() == 20
    assert s2.pop() == 10
    assert s2.is_empty()

    # iteration is non-destructive
    s3 = Stack.from_list([1, 2, 3])
    values = list(s3)
    print(f"Iterate top->bottom: {values}")
    assert values == [3, 2, 1]
    assert len(s3) == 3          # still intact

    # error handling
    empty = Stack()
    try:
        empty.pop()
        raise AssertionError("should have raised")
    except IndexError:
        pass

    try:
        empty.peek()
        raise AssertionError("should have raised")
    except IndexError:
        pass

    print()
    print("All Stack demos and assertions passed.")
