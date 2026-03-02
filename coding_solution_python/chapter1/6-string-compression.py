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
    prev_letter_count = 1
    for s in string_in:
        if s != prev_letter:
            if prev_letter:
                res.append(f"{prev_letter}{str(prev_letter_count)}")
            prev_letter = s
            prev_letter_count = 1
        else:
            prev_letter = s
            prev_letter_count += 1
    res.append(f"{prev_letter}{str(prev_letter_count)}")
    res = "".join(res)
    if len(res) >= len(string_in):
        return string_in
    else:
        return res

def test_func(string_in, expected_result):
    res = string_compression(string_in)
    if res != expected_result:
        raise ValueError(f"Error - {string_in} returns {res}, expected {expected_result}!")


if __name__ == "__main__":
    test_func("aabcccccaaa", "a2b1c5a3")
    test_func("aab", "aab")