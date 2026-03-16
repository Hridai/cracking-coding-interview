"""
Problem:
Given an image represented by an NxN matrix, where each pixel in the image is
4 bytes, write a method to rotate the image by 90 degrees. Can you do this
in place?
"""

"""
Questions:
Which direction — clockwise or counter-clockwise? Assuming clockwise.
Can we use extra space? The problem asks for in-place, so no O(N²) copy.

Algorithm:
Rotate the matrix layer by layer (concentric rings), from outermost to innermost.
There are N//2 layers total.

For each layer, iterate along the top edge. For each position i in that edge,
perform a 4-way swap using one temp variable:

  top    → temp
  left   → top
  bottom → left
  right  → bottom
  temp   → right

Index mapping for a clockwise 90° rotation of cell (r, c) in an NxN matrix:
  (r, c) → (c, N-1-r)

For a layer starting at offset `first` with last index `last`, and position `i`
steps into the edge:
  top    = matrix[first][first + i]
  right  = matrix[first + i][last]
  bottom = matrix[last][last - i]
  left   = matrix[last - i][first]

Time complexity:  O(N²) — every cell is touched once
Space complexity: O(1) — single temp variable, in-place
"""


def rotate_matrix(matrix):
    n = len(matrix)
    for layer in range(n // 2):
        first = layer
        last = n - 1 - layer
        for i in range(last - first):
            temp = matrix[first][first + i]          # save top
            matrix[first][first + i] = matrix[last - i][first]       # left → top
            matrix[last - i][first] = matrix[last][last - i]         # bottom → left
            matrix[last][last - i] = matrix[first + i][last]         # right → bottom
            matrix[first + i][last] = temp                           # temp → right
    return matrix


def test_func(matrix, expected):
    result = rotate_matrix(matrix)
    if result != expected:
        raise Exception(f"Test failed!\n  got:      {result}\n  expected: {expected}")


if __name__ == "__main__":
    # 2x2
    test_func(
        [[1, 2],
         [3, 4]],
        [[3, 1],
         [4, 2]]
    )

    # 3x3
    test_func(
        [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]],
        [[7, 4, 1],
         [8, 5, 2],
         [9, 6, 3]]
    )

    # 4x4
    test_func(
        [[ 1,  2,  3,  4],
         [ 5,  6,  7,  8],
         [ 9, 10, 11, 12],
         [13, 14, 15, 16]],
        [[13,  9,  5,  1],
         [14, 10,  6,  2],
         [15, 11,  7,  3],
         [16, 12,  8,  4]]
    )

    # 1x1 — no rotation needed
    test_func([[42]], [[42]])

    print("All tests passed.")
