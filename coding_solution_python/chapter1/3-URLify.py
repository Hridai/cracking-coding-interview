"""
Problem:
Write a method to replace all spaces in a string with '%20'. You may assume that the string has 
sufficient space at the end to hold the additional characters, and that you are given the "true"
length of the string.
"""

"""
Questions:


Algorithm:
- Option 1:
    Iterate over the string, check if it's a space, if it's a space, insert "%20" into it
    Given a strings immutability, you will have to write this to another "result" array
    and then parse them into a string. The space complexity is 2n, time complexity n

- Option 2:
    Built-in string replace() function

- Option 3:
    split() function on a string, then join() function with "%20"

"""


def urlify(s, true_length):
    space_count = sum(1 for i in range(true_length) if s[i] == " ")
    chars = list(s[:true_length] + " " * (space_count * 2))

    i = true_length - 1
    j = len(chars) - 1

    while i >= 0:
        if chars[i] == " ":
            chars[j] = "0"
            chars[j - 1] = "2"
            chars[j - 2] = "%"
            j -= 3
        else:
            chars[j] = chars[i]
            j -= 1
        i -= 1

    return "".join(chars)


def test(input_str, true_length, expected):
    result = urlify(input_str, true_length)
    if result != expected:
        raise Exception(f"FAIL: urlify({input_str!r}) => {result!r}, expected {expected!r}")


if __name__ == "__main__":
    test("Mr John Smith", 13, "Mr%20John%20Smith")
    test("hiya ", 4, "hiya")
    test("hiya ", 5, "hiya%20")
    test("   ", 3, "%20%20%20")
    test("", 0, "")
    test("nospaces", 8, "nospaces")
    print("All tests passed.")
