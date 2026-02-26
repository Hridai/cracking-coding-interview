"""
Problem:
There are three types of edits that can be performed on strings: insert a
character, remove a character, or replace a character. Given two strings,
write a function to check if they are one edit (or zero edits) away.

Example:
pale,  ple  → true
pales, pale → true
pale,  bale → true
pale,  bake → false
"""

"""
Questions:
How do we want spaces, and non-alphabetical characters to be treated?

What about the character cases? I will assume we are only dealing with
alphabetical characters. Also will assume case insensitivity, will
assume everything is lower case.

Algorithm:
1. Normalise both strings: strip non-alpha characters and lowercase.
2. Fast path: if the length difference is greater than 1, return False.
3. Same length: walk both strings in parallel and count mismatches.
   At most 1 mismatch allowed (0 = identical, 1 = one replacement).
4. Length differs by 1: two-pointer walk through the shorter string,
   allowing one skip in the longer string. If a second mismatch is
   found after the skip, return False.

Time complexity: O(n)
Space complexity: O(n) for the two normalised strings, O(1) extra for
the algorithm itself (no additional data structures).

"""

def one_away(string_1, string_2):
    string_1 = ''.join(c for c in string_1 if c.isalpha()).lower()
    string_2 = ''.join(c for c in string_2 if c.isalpha()).lower()
    if abs(len(string_1) - len(string_2)) > 1:
        return False

    count_diffs = 0
    if len(string_1) == len(string_2):
        for s1, s2 in zip(string_1, string_2):
            if s1 != s2:
                count_diffs += 1
        return True if count_diffs <= 1 else False

    longer_string = string_1
    shorter_string = string_2
    if len(string_2) > len(string_1):
        longer_string = string_2
        shorter_string = string_1

    diff_found = False
    for i, _ in enumerate(shorter_string):
        longer_str_index = i + 1 if diff_found else i
        if shorter_string[i] != longer_string[longer_str_index]:
            if diff_found:
                return False
            else:
                diff_found = True
                if shorter_string[i] != longer_string[i+1]:
                    return False

    return True


def test_func(string_1, string_2, expected_result):
    res = one_away(string_1, string_2)
    if res != expected_result:
        raise Exception(f"Test failed for {string_1}, {string_2}!")


if __name__ == "__main__":
    test_func("pale", "ple", True)
    test_func("pales", "pale", True)
    test_func("pale", "bale", True)
    test_func("pale", "bake", False)
    test_func("pale", "pale", True)
    test_func("a", "b", True)
    test_func("aab", "bba", False)
    test_func("", "", True)
    test_func("", "a", True)
    test_func("", "aa", False)
    test_func("aa", "!aa", True)
    test_func("AA", "!aa", True)
