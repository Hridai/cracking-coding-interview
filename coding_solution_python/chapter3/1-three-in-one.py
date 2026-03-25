"""
Problem:
Describe how you could use a single array to implement three stacks.
"""

"""
Questions:


Algorithm:
In a class, i will have a python list, initialised with empty strings up to n
Track the three stack top pointers and write push / pop functions with respect
to these, flooring and capping the pointers w.r.t the stack size.

Value error is thrown if a stack is full. Preallocate memory using None objects
in a python list to give a fixed length.

"""


class ThreeStack:
    def __init__(self, stack_size=4):
        self.stack_size = stack_size
        self.data = [None] * (stack_size * 3)
        self.top_pointers = [0, stack_size, stack_size * 2]

    def push(self, stack_number, value):
        """stack number is 0 indexed"""
        stack_top_bound = ((stack_number + 1) * self.stack_size)
        if self.top_pointers[stack_number] >= stack_top_bound:
            raise ValueError(f"Stack index {stack_number} is full")
        self.data[self.top_pointers[stack_number]] = value
        self.top_pointers[stack_number] += 1

    def pop(self, stack_number):
        """stack number is 0 indexed; returns the popped value"""
        stack_bottom_bound = stack_number * self.stack_size
        if self.top_pointers[stack_number] <= stack_bottom_bound:
            raise ValueError(f"Stack index {stack_number} is already empty")
        self.top_pointers[stack_number] -= 1
        value = self.data[self.top_pointers[stack_number]]
        self.data[self.top_pointers[stack_number]] = None
        return value

    def __repr__(self):
        return str(self.data)

if __name__ == "__main__":
    # Basic push/pop on a single stack
    s = ThreeStack(stack_size=3)
    s.push(0, 10)
    s.push(0, 20)
    assert s.pop(0) == 20
    assert s.pop(0) == 10

    # All three stacks operate independently
    s = ThreeStack(stack_size=3)
    s.push(0, "a")
    s.push(1, "b")
    s.push(2, "c")
    assert s.pop(0) == "a"
    assert s.pop(1) == "b"
    assert s.pop(2) == "c"

    # Interleaved pushes and pops don't bleed between stacks
    s = ThreeStack(stack_size=3)
    s.push(0, 1)
    s.push(1, 2)
    s.push(0, 3)
    assert s.pop(0) == 3
    assert s.pop(1) == 2
    assert s.pop(0) == 1

    # Push to full stack raises ValueError
    s = ThreeStack(stack_size=2)
    s.push(0, 1)
    s.push(0, 2)
    try:
        s.push(0, 3)
        raise Exception("Expected ValueError for full stack")
    except ValueError:
        pass

    # Pop from empty stack raises ValueError
    s = ThreeStack(stack_size=2)
    try:
        s.pop(1)
        raise Exception("Expected ValueError for empty stack")
    except ValueError:
        pass

    # Pop returns correct value after filling and draining
    s = ThreeStack(stack_size=3)
    for i in range(3):
        s.push(2, i)
    assert s.pop(2) == 2
    assert s.pop(2) == 1
    assert s.pop(2) == 0

    print("All tests passed")
