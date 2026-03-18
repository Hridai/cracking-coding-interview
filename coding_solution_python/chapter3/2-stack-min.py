"""
Problem:
How would you design a stack which, in addition to push and pop, has a
function min which returns the minimum element? Push, pop and min should all
operate in O(1) time.
"""

"""
Questions:


Algorithm:


"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'utils'))
from stack import Stack


def func_to_write():
    pass


def test_func(x, expected_result):
    res = func_to_write()
    if res != expected_result:
        raise ValueError(f"Result {res} does not match expected result {expected_result}")


if __name__ == "__main__":
    test_func("x", "expected_result")
