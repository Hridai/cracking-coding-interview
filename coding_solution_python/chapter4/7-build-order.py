"""
Problem:
You are given a list of projects and a list of dependencies (which is a list
of pairs of projects, where the second project is dependent on the first
project). All of a project's dependencies must be built before the project is.
Find a build order that will allow the projects to be built. If there is no
valid build order, return an error.

EXAMPLE:
Input:
  projects: a, b, c, d, e, f
  dependencies: (a, d), (f, b), (b, d), (f, a), (d, c)
Output: f, e, a, b, d, c
"""

"""
Questions:


Algorithm:


"""

def func_to_write():
    pass


def test_func(x, expected_result):
    res = func_to_write()
    if res != expected_result:
        raise ValueError(f"Result {res} does not match expected result {expected_result}")


if __name__ == "__main__":
    test_func("x", "expected_result")
