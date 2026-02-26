"""
Problem:
Given a string, write a function to check if it is a permutation of a
palindrome, A palindrome is a word or phrase that is the same forwards
and backwards. A permutation is a rearrangement of letters. The palindrome
does not need to be limited to just dictionary words. You can ignore casing
and non-letter characters

Example:
Input: Tact Coa
Output: True (permutations "taco cat", "atco cta")
"""

"""
Questions:


Algorithm:
My approach will iterate over every character in the string and save the counts
to a hash-map of the letter and the counts of that letter in the string.

If all counts are even, except one, then we have a palindrome, as we would be
able to print the count of each letter, divided by 2, then all the odd letters
in the middle of the string, forming the pivot of the palindrome, before printing
in the exact reverse order the other letters, forming the palindrome.

The time complexity is O(n) as you iterate over a string. The space complexity is
O(1) as you need a hash-map, and then possibly a new string to write to, depending
on the language. The input size is O(n) but the dictionary needed to track the
character count is O(1), resulting in a total space used of O(n).

"""


def palindome_checker(str_in):
    d = {}
    for char in str_in.lower():
        if not char.isalpha():
            continue
        if char in d:
            d[char] += 1
        else:
            d[char] = 1
    
    odd_exist = False
    for k, v in d.items():
        if v % 2 == 1:
            if odd_exist:
                return False  # can't have more than one odd numbered count for a letter in the string if a palindrome
            odd_exist = True
    
    return True


def palindrome_checker_bits(s):
    """
    NOTE: I did not write this function. This is the optimised bit-vector solution
    that I need to study and understand. See 'bit-vector-explainer.md' in this
    folder for a full breakdown of how it works.

    Uses a single integer as 26 on/off switches (one per alphabet letter).
    XOR-toggles the bit for each character seen. A character seen an even number
    of times cancels itself out (bit returns to 0). At the end, at most one bit
    may remain set for the string to be a valid palindrome permutation.
    """
    bits = 0
    for char in s.lower():
        if char.isalpha():
            bits ^= (1 << (ord(char) - ord('a')))
    return bits == 0 or (bits & (bits - 1)) == 0


def test_palindrome_checker(str_in, expected_result):
    res = palindome_checker(str_in)
    if res != expected_result:
        raise Exception(f"Test failed for {str_in}")

if __name__ == "__main__":
    test_palindrome_checker("Tact Coa", True)
    test_palindrome_checker("  Tact   Coa  ", True)
    test_palindrome_checker("aaabbbccc", False)
    test_palindrome_checker("A", True)
    test_palindrome_checker("A!!!!", True)
    test_palindrome_checker(" ", False)
