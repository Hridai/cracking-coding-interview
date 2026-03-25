"""
Problem:
How would you design a stack which, in addition to push and pop, has a
function min which returns the minimum element? Push, pop and min should all
operate in O(1) time.
"""

"""
Questions:
- Are elements comparable (i.e. can we use < on them)?
- Can the stack hold duplicate values?

Algorithm:
Maintain a second "min stack" that shadows the main stack.
- push(x): push x to main; push min(x, current_min) to min stack
- pop(): pop both stacks; return value from main stack
- min(): peek the min stack — O(1)

Each slot in the min stack stores the minimum of all elements at or below
that position, so popping the current minimum simply reveals the previous
minimum at the top of the min stack. All three operations are O(1).

Time:  O(1) push, pop, min
Space: O(n) extra for the min stack
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'utils'))
from stack import Stack


class MinStack:
    def __init__(self):
        self._stack = Stack()
        self._min_stack = Stack()

    def push(self, value):
        self._stack.push(value)
        new_min = value if self._min_stack.is_empty() else min(value, self._min_stack.peek())
        self._min_stack.push(new_min)

    def pop(self):
        self._min_stack.pop()
        return self._stack.pop()

    def min(self):
        if self._min_stack.is_empty():
            raise IndexError("min of empty stack")
        return self._min_stack.peek()


if __name__ == "__main__":
    # Basic min tracking
    s = MinStack()
    s.push(5)
    assert s.min() == 5
    s.push(3)
    assert s.min() == 3
    s.push(7)
    assert s.min() == 3  # 7 doesn't displace 3

    # Popping the current min restores the previous min
    s.push(1)
    assert s.min() == 1
    assert s.pop() == 1
    assert s.min() == 3  # restored correctly

    # Popping a non-min value doesn't change min
    assert s.pop() == 7
    assert s.min() == 3

    # Draining the stack
    assert s.pop() == 3
    assert s.min() == 5
    assert s.pop() == 5

    # Duplicate values — both pushes and pops should work cleanly
    s2 = MinStack()
    s2.push(2)
    s2.push(2)
    assert s2.min() == 2
    s2.pop()
    assert s2.min() == 2  # duplicate; min should still be 2

    # min on empty stack raises
    empty = MinStack()
    try:
        empty.min()
        raise Exception("Expected IndexError")
    except IndexError:
        pass

    print("All tests passed")
