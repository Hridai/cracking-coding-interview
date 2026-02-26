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


def urlify(str_in, expected_result):
    print(f"running {str_in}")
    res = []
    for s in str_in:
        res.append("%20") if s == " " else res.append(s)
    res = "".join(res)
    print(f"result: {res}")
    if res == expected_result:
        print("True")
        return True
    else:
        print("False")
        return False

if __name__ == "__main__":
    urlify("hiya", "hiya")
    urlify("hiya ", "hiya%20")
