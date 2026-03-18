"""
Problem:
The similarity of two documents (each with distinct words) is defined to be
the size of the intersection divided by the size of the union. For example,
if the documents consist of integers {1, 5, 3} and {1, 7, 2, 3}, the
intersection is {1, 3} and the union is {1, 2, 3, 5, 7}, giving a similarity
of 2/5 = 0.4. We have a long list of documents (with distinct words) and wish
to find every pair of documents with similarity greater than 0. Print all such
pairs along with their similarity.

EXAMPLE:
Input:  13: {14, 15, 100, 9, 3}, 16: {32, 1, 9, 3, 5}, 19: {15, 29, 2, 6, 8, 7},
        24: {7, 10}
Output: ID1, ID2 : SIMILARITY
        13, 19  : 0.1
        13, 16  : 0.25
        19, 24  : 0.14285714285714285
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
