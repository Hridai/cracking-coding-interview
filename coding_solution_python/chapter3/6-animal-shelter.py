"""
Problem:
An animal shelter, which holds only dogs and cats, operates on a strictly
"first in, first out" basis. People must adopt either the "oldest" (based on
arrival time) of all animals at the shelter, or they can select whether they
would prefer a dog or a cat (and will receive the oldest animal of that type).
They cannot select which specific animal they would like. Create the data
structures to maintain this system and implement operations such as enqueue,
dequeueAny, dequeueDog, and dequeueCat.
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
