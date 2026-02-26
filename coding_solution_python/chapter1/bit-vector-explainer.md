# Bit Vectors — How and Why

Written as a companion to the bit-vector solution in `4-palindrome-permutation.py`.

---

## The Problem Context

For palindrome permutation checking, we need to track whether each letter has been
seen an odd or even number of times. The naive approach is a dict with up to 26 keys.
The bit-vector approach does the same thing with a **single integer**.

---

## `ord()` — Turning a Character Into a Number

Every character has a numeric code (its ASCII value). `ord()` gives you that number.

```python
ord('a')  # → 97
ord('b')  # → 98
ord('z')  # → 122
```

We subtract `ord('a')` to get a 0-based index into the alphabet:

```python
ord('a') - ord('a')  # → 0   (slot 0)
ord('b') - ord('a')  # → 1   (slot 1)
ord('c') - ord('a')  # → 2   (slot 2)
```

So every letter maps to a unique integer 0–25. This is how we pick which "switch" to flip.

---

## The Bit Vector — One Integer, 26 Switches

An integer is just a sequence of bits (0s and 1s). We treat each bit position as an
on/off switch for one letter:

```
bit position:  25 24 23 ... 2  1  0
letter:         z  y  x  ... c  b  a
```

We start with `bits = 0` — all switches OFF:

```
bits = 0b00000000000000000000000000
```

---

## `^=` — XOR Toggle

`^` is the **XOR** (exclusive-or) operator. Applied to two bits:

```
0 ^ 0 = 0   (both same → 0)
1 ^ 1 = 0   (both same → 0)
0 ^ 1 = 1   (different → 1)
1 ^ 0 = 1   (different → 1)
```

The critical property: **XORing any bit with 1 flips it.**

```python
bits ^= (1 << index)
```

`1 << index` shifts the number `1` left by `index` positions, creating a number
with exactly one `1` bit at position `index`. XORing that into `bits` toggles
just that one switch — ON if it was OFF, OFF if it was ON.

This means:
- First time we see letter `x` → toggle ON  (odd count)
- Second time we see letter `x` → toggle OFF (even count, cancels out)
- Third time → ON again, and so on

---

## Walking Through `"aab"`

```
Start:  bits = 0  →  ...000000

See 'a' (index 0):  bits ^= (1 << 0)  →  ...000001   ('a' seen 1 time, odd)
See 'a' (index 0):  bits ^= (1 << 0)  →  ...000000   ('a' seen 2 times, even — cancelled)
See 'b' (index 1):  bits ^= (1 << 1)  →  ...000010   ('b' seen 1 time, odd)

Final bits = 0b10
```

Only 'b' has a bit set, meaning only 'b' has an odd count.
`"aab"` can be rearranged to `"aba"` — a valid palindrome.

---

## The Final Check

For a palindrome permutation, **at most one character can have an odd count**
(it sits in the middle of the palindrome).

```python
bits == 0                    # all even → valid (even-length palindrome, e.g. "abba")
bits & (bits - 1) == 0      # exactly one bit set → valid (odd-length, e.g. "aba")
```

### Why does `bits & (bits - 1) == 0` detect exactly one bit?

Subtracting 1 from a number flips the lowest set bit to 0 and all bits below it to 1.
ANDing with the original clears that lowest bit. If the result is 0, there was only
one bit set to begin with.

Example with one bit set:
```
bits     = 0b0100   (4)
bits - 1 = 0b0011   (3)
AND      = 0b0000   → zero ✓ exactly one bit
```

Example with two bits set:
```
bits     = 0b0110   (6)
bits - 1 = 0b0101   (5)
AND      = 0b0100   → not zero ✗ more than one bit
```

---

## The Full Function

```python
def palindrome_checker_bits(s):
    bits = 0
    for char in s.lower():
        if char.isalpha():
            bits ^= (1 << (ord(char) - ord('a')))
    return bits == 0 or (bits & (bits - 1)) == 0
```

One pass. One integer. No dict.

---

## Why This Matters in an Interview

| | Dict approach | Bit vector |
|---|---|---|
| Extra space | O(1) — up to 26 keys | O(1) — one integer |
| Memory (actual) | ~26 dict entries | 1 integer (a few bytes) |
| Interview signal | Solid understanding | Low-level systems thinking |

The asymptotic complexity is the same, but the bit vector demonstrates that you can
think about data packing and binary representation — a signal that stands out.

**Say in an interview:** "I can also solve this with a single integer used as a bit
vector, toggling each letter's bit with XOR. At the end I check that at most one
bit is set. It's the same O(n) time and O(1) space, but with a much smaller constant."
