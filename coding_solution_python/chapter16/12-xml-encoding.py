"""
Problem:
Since XML is very verbose, you are given a way of encoding it where each tag
gets mapped to a pre-defined integer value. The language/grammar is as
follows:
  Element   --> Tag Attributes END Children END
  Attribute --> Tag Value
  END       --> 0
  Tag       --> some predefined mapping to int
  Value     --> string value
For example: family --> 1, person --> 2, firstName --> 3, lastName --> 4,
state --> 5. Implement a method encode(String xml) which encodes the above XML.
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
