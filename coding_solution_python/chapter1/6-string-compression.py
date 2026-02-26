"""
Problem:
Implement a method to perform basic string compression using the counts of
repeated characters. For example, the string aabcccccaaa would become a2b1c5a3.
If the compressed string would not be smaller than the original string, your
method should return the original string. You can assume the string has only
uppercase and lowercase letters.
"""

"""
Questions:
Are we assuming lower case and upper case values are not equal. This is the
assumption I am making in my solution.

Algorithm:
O(n) time complexity. We will iterate over the string and keep a running total
of the characters and their counts.

At the very end, we will do a len() check of the initial input and the final
output and see which is longer. If input is shorter, we will simply return
that.

"""

def string_compression(string_in):
    res = []
    prev_letter = ""
    prev_letter_count = 0
    for s in string_in:
        if s == prev_letter:
            


def test_func():
    return func()


if __name__ == "__main__":
    test_func()