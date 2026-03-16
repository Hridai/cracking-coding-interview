"""
Problem:
Assume you have a method isSubstring which checks if one word is a substring
of another. Given two strings, s1 and s2, write code to check if s2 is a
rotation of s1 using only one call to isSubstring (e.g., "waterbottle" is a
rotation of "erbottlewat").
"""

"""
Questions:
Can we assume everything is lower case? Yes.
Can we ignore non-alpha characters? No — rotation is defined on the full string.

Algorithm:
A rotation of s1 is s1 split at some index i and rejoined: s1[i:] + s1[:i].
Every such rotation appears as a substring of s1+s1.
So: check len(s1) == len(s2), then check if s2 is a substring of s1+s1.
Time: O(n), Space: O(n) for the doubled string.
"""

def is_substring(s, sub):
    return sub in s


def string_rotation(str1, str2):
    if len(str1) != len(str2):
        return False
    return is_substring(str1 + str1, str2)


def test_func(str1, str2, expected_result):
    res = string_rotation(str1, str2)
    if res != expected_result:
        raise ValueError(f"{str1} is not a rotation of {str2} - got result {res} but expected {expected_result}")


if __name__ == "__main__":
    test_func("waterbottle", "erbottlewat", True)
    test_func("waterbottle", "rbottlewat", False)
    test_func("waterbottle", "zrbottlewat", False)
    test_func("waterbottle", "21erbottlewat", False)
    test_func("", "", True)
    test_func("", "a", False)
    test_func("a", "a", True)
    test_func("abc", "abc", True)
    test_func("aab", "aba", True)
    print("All tests passed.")